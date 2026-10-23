# Fase 3 · Su copia de OpenReply en GitHub

**Para qué:** su servidor necesita OpenReply «empaquetado» (una imagen de
Docker). Construirlo en el servidor lo dejaría sin aire durante minutos, así
que lo construye GitHub, gratis, en su propia cuenta. Y al ser su copia, no
depende de nadie.

La versión es siempre la de `docs/version.md`. No uses la última de OpenReply
sin probar: cambia rápido.

## Camino con terminal (si tiene `git` y `gh` con sesión iniciada)

Tú lo haces, ella mira:

```bash
gh repo fork diwenne/openreply --clone=true --remote=false
cd openreply
git checkout -b instalacion dca8713          # la versión de docs/version.md
mkdir -p .github/workflows
cp RUTA-A-ESTE-REPO/plantillas/publicar-imagen.yml .github/workflows/
git add .github/workflows/publicar-imagen.yml
git commit -m "Publicar imagen en GHCR"
git push -u origin instalacion
```

## Camino por la web (sin terminal)

Un clic por turno, con captura si duda:

1. En github.com/diwenne/openreply, botón **Fork** → **Create fork**.
2. En su copia, entra a la versión fijada: `github.com/SU-USUARIO/openreply/tree/dca8713`.
3. En el desplegable de ramas, escribe `instalacion` y pulsa **Create branch
   instalacion from dca8713**.
4. En esa rama: **Add file → Create new file**, nombre
   `.github/workflows/publicar-imagen.yml`, y pega el contenido de
   `plantillas/publicar-imagen.yml` (cárgaselo tú en el portapapeles). **Commit changes**.

## Trampa: en los forks, Actions viene apagado

Pestaña **Actions** de su copia. Si sale «Workflows aren't being run on this
forked repository», que pulse **I understand my workflows, go ahead and enable
them**. Si la construcción no arrancó sola: **Publicar imagen (GHCR) → Run
workflow → rama `instalacion`**.

Tarda de 5 a 10 minutos. Espera a que salga en verde.

## Hacer la imagen pública

Su perfil de GitHub → **Packages → openreply → Package settings → Change
visibility → Public**. Así su servidor la descarga sin contraseña. La imagen
no lleva ninguna clave: las claves van en el `.env` del servidor.

## Lo que se guarda

En el progreso: `ghcr.io/SU-USUARIO/openreply:sha-xxxxxxx` (la etiqueta sale
en la página del paquete). Ese es su `OPENREPLY_IMAGE`. No es un secreto.

## Comprobación

```bash
docker manifest inspect ghcr.io/SU-USUARIO/openreply:sha-xxxxxxx > /dev/null && echo "imagen pública y descargable"
```

Sin Docker en su ordenador, basta con abrir la página del paquete en una
ventana privada del navegador: si la ve sin iniciar sesión, es pública.
