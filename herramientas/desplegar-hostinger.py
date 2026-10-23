#!/usr/bin/env python3
"""Despliega OpenReply en un VPS de Hostinger por su API, sin mostrar ninguna clave.

Las claves salen de 1Password (CLI `op`) y viajan directas al servidor: no se
imprimen, no se guardan en el repo y no pasan por ningún chat. Lo que no es
secreto (dominio, imagen, correos) se pasa por parámetros.

Frenos:
- Si ya existe un proyecto con ese nombre, se para: en Hostinger, crear un
  proyecto con un nombre existente lo REEMPLAZA (por ejemplo, n8n). Para
  volver a desplegar el propio OpenReply, añade --reemplazar.
- Comprueba el formato de las claves antes de enviar nada.

Ejemplo:
  herramientas/desplegar-hostinger.py --vm 1234567 \\
    --compose plantillas/docker-compose.solo.yml \\
    --item "op://Private/OpenReply-servidor" \\
    --dominio openreply.tudominio.com \\
    --imagen ghcr.io/mi-usuario/openreply:sha-1234567 \\
    --correos "tu@correo.com" --remitente "OpenReply <panel@tudominio.com>"
"""
import argparse, json, os, re, subprocess, sys, time, urllib.error, urllib.request

API = "https://developers.hostinger.com"
OBLIGATORIAS = ["NEXTAUTH_SECRET", "CRON_SECRET", "ENCRYPTION_KEY", "POSTGRES_PASSWORD", "WEBHOOK_VERIFY_TOKEN"]
OPCIONALES = ["INSTAGRAM_APP_ID", "INSTAGRAM_APP_SECRET", "FACEBOOK_APP_SECRET", "EMAIL_SERVER", "RESEND_API_KEY"]
TRAEFIK = ["TRAEFIK_RED", "TRAEFIK_ENTRADA", "TRAEFIK_CERTIFICADOS"]


def parar(msg):
    sys.exit("✗ " + msg)


def leer_op(ref, obligatoria):
    r = subprocess.run(["op", "read", ref], capture_output=True, text=True)
    if r.returncode != 0:
        if obligatoria:
            parar(f"no pude leer {ref.rsplit('/', 1)[-1]} de 1Password (¿existe el campo? ¿sesión abierta?)")
        return ""
    return r.stdout.strip()


def api(token, metodo, ruta, cuerpo=None):
    req = urllib.request.Request(API + ruta, method=metodo,
                                 data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        parar(f"Hostinger respondió {e.code}: {e.read().decode()[:300]}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--vm", required=True, help="ID del VPS en Hostinger")
    p.add_argument("--compose", required=True, help="plantillas/docker-compose.solo.yml o .traefik.yml")
    p.add_argument("--item", required=True, help='elemento de 1Password, ej. "op://Private/OpenReply-servidor"')
    p.add_argument("--dominio", required=True)
    p.add_argument("--imagen", required=True)
    p.add_argument("--correos", required=True, help="ALLOWED_EMAILS, separados por comas")
    p.add_argument("--remitente", required=True, help='EMAIL_FROM, ej. "OpenReply <panel@tudominio.com>"')
    p.add_argument("--proyecto", default="openreply")
    p.add_argument("--reemplazar", action="store_true", help="solo para volver a desplegar ESTE mismo proyecto")
    a = p.parse_args()

    if not re.fullmatch(r"[a-z0-9][a-z0-9_]*", a.proyecto):
        parar("el nombre del proyecto solo admite minúsculas, números y _ (sin guiones)")
    item = a.item.rstrip("/")
    token = leer_op(item + "/HOSTINGER_API_TOKEN", True)

    existentes = api(token, "GET", f"/api/vps/v1/virtual-machines/{a.vm}/docker")
    existentes = existentes if isinstance(existentes, list) else existentes.get("data", [])
    nombres = [x.get("name") for x in existentes]
    if a.proyecto in nombres and not a.reemplazar:
        parar(f"ya existe un proyecto «{a.proyecto}» en ese VPS ({', '.join(nombres)}). "
              "Desplegar con ese nombre lo REEMPLAZARÍA. Usa otro nombre, o --reemplazar si es tu propio OpenReply.")

    env = {k: leer_op(f"{item}/{k}", True) for k in OBLIGATORIAS}
    env.update({k: leer_op(f"{item}/{k}", False) for k in OPCIONALES})
    env.update({"DOMINIO": a.dominio, "OPENREPLY_IMAGE": a.imagen, "ALLOWED_EMAILS": a.correos, "EMAIL_FROM": a.remitente})
    env.update({k: os.environ[k] for k in TRAEFIK if os.environ.get(k)})

    if not re.fullmatch(r"[0-9a-f]{64}", env["ENCRYPTION_KEY"]):
        parar("ENCRYPTION_KEY tiene que ser de 64 caracteres hexadecimales (openssl rand -hex 32)")
    if not (env["EMAIL_SERVER"] or env["RESEND_API_KEY"]):
        parar("falta el correo: EMAIL_SERVER o RESEND_API_KEY en 1Password")
    for k, v in env.items():
        if k == "EMAIL_FROM":
            continue
        if any(c in v for c in "\n$' \""):
            parar(f"{k} tiene un espacio, comilla, $ o salto de línea: genera otra con solo letras y números")

    with open(a.compose) as f:
        compose = f.read()
    cuerpo = {"project_name": a.proyecto, "content": compose,
              "environment": "".join(f'{k}={v}\n' if " " not in v else f'{k}="{v}"\n' for k, v in env.items() if v)}
    # El cuerpo va directo a la API, en memoria: nunca se escribe a disco.
    accion = api(token, "POST", f"/api/vps/v1/virtual-machines/{a.vm}/docker", cuerpo)
    del cuerpo, env

    aid = accion.get("id")
    print(f"✓ despliegue enviado (acción {aid}). Esperando a Hostinger…")
    for _ in range(36):
        estado = api(token, "GET", f"/api/vps/v1/virtual-machines/{a.vm}/actions/{aid}").get("state")
        if estado in ("success", "error"):
            break
        time.sleep(5)
    print(f"{'✓' if estado == 'success' else '✗'} Hostinger: {estado}")
    print(f"Ahora comprueba: curl -s https://{a.dominio}/api/health  (la primera vez tarda hasta 90 s)")
    sys.exit(0 if estado == "success" else 1)


if __name__ == "__main__":
    main()
