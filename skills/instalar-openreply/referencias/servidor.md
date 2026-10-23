# Fase 5 · Su servidor

**Para qué:** OpenReply tiene que estar encendido las 24 horas en internet,
para que Instagram le avise de cada comentario. Eso es un servidor.

## A · No tiene servidor → VPS de Hostinger

1. **La cuenta:** si no tiene cuenta en Hostinger, puede usar el enlace del
   autor de esta guía: https://www.hostinger.com/es?REFERRALCODE=GQAHJSOLIIPU.
   **Díselo tal cual: es un enlace de afiliado**, el autor recibe una comisión
   y a ella no le cuesta más. Que elija.
   **El plan:** el VPS más pequeño (KVM 1: 1 procesador, 4 GB) sobra.
   OpenReply usa menos de 1 GB. Sistema: **Ubuntu con Docker** (la plantilla
   de Docker). Si además quiere n8n algún día, puede elegir la plantilla de n8n
   y seguir el camino B.
2. **Su dirección.** En el panel del VPS sale un nombre del tipo
   `srvXXXXXXX.hstgr.cloud` que ya apunta a su servidor. Le sirve como
   `DOMINIO` sin tocar nada. Si prefiere su dominio, crea un registro A que
   apunte a la IP del VPS. Compruébalo antes de seguir:
   `dig +short SU-DOMINIO` (o `nslookup SU-DOMINIO`) tiene que dar la IP del VPS.
3. **El despliegue**, por uno de estos dos caminos:

   **A1 · Por el panel (sin terminal).** VPS → **Docker Manager** → crear
   proyecto / Compose:
   - Nombre del proyecto: `openreply`.
   - El contenido: `plantillas/docker-compose.solo.yml`. Cárgaselo en el
     portapapeles.
   - Las variables de entorno: dale la lista de **nombres** de
     `plantillas/env.example`, de una en una:
     - las que no son secretas (`DOMINIO`, `OPENREPLY_IMAGE`, `ALLOWED_EMAILS`,
       `EMAIL_FROM`) se las cargas tú en el portapapeles;
     - las secretas las copia ella de 1Password.
   - Desplegar.

   **A2 · Por la API (con la CLI de 1Password).** Ella crea en Hostinger un
   token de API (hPanel → su perfil → API) y lo guarda en 1Password como
   `HOSTINGER_API_TOKEN`. Tú ejecutas:
   ```bash
   python3 herramientas/desplegar-hostinger.py --vm ID_DEL_VPS --compose plantillas/docker-compose.solo.yml \
     --item "op://Private/OpenReply-servidor" --dominio SU-DOMINIO \
     --imagen ghcr.io/SU-USUARIO/openreply:sha-xxxxxxx --correos "tu@correo.com" \
     --remitente "OpenReply <panel@tudominio.com>"
   ```
   El script lee las claves de 1Password y las manda al servidor sin
   mostrarlas. El ID del VPS sale en la API (`GET /api/vps/v1/virtual-machines`)
   o en la dirección del panel.

4. **Comprueba** con `referencias/verificacion.md`. Que pase la salud antes de
   seguir.

## B · Ya tiene n8n de Hostinger (u otro Traefik)

Usa `plantillas/docker-compose.traefik.yml`. OpenReply se mete detrás del
Traefik que ya existe, **sin tocar n8n**.

- Su dirección: un subdominio que apunte al mismo VPS (con la de Hostinger,
  `openreply.srvXXXXXXX.hstgr.cloud` suele funcionar sin tocar DNS).
  Compruébalo con `dig`.
- Los valores por defecto `TRAEFIK_*` son los de la plantilla de n8n de
  Hostinger. Si su Traefik es otro, mira en su compose el nombre de la red, la
  entrada https y el «certresolver».
- 🔴 **El proyecto se llama `openreply`, nunca como el de n8n.** En Hostinger,
  crear un proyecto con un nombre que ya existe **lo reemplaza**.
- **No reinicies n8n** ni toques su compose.

## C · Otro servidor con Docker y acceso por terminal

`docker-compose.solo.yml` si los puertos 80 y 443 están libres (si no, el de
Traefik). El `.env` se crea **en el servidor**, nunca en el chat:
- con la CLI de 1Password en el servidor, `op inject -i env.tpl -o .env`;
- o a mano, copiando de 1Password.

Después, `docker compose -p openreply up -d`.

## Trampas del servidor

- Redesplegar el mismo proyecto **conserva los datos**, pero reinicia los
  contenedores (unos 40 segundos sin panel).
- La primera vez el panel tarda hasta 90 segundos en responder: está
  preparando la base de datos. Un error 502 en ese rato es normal.
