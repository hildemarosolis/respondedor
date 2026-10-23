# Comprobar de verdad

«Listo» no prueba nada. Estas son las comprobaciones de cada fase, y qué hacer
si fallan.

## Comprobaciones

| Qué | Cómo | Bien si… |
|---|---|---|
| La dirección apunta al servidor | `dig +short SU-DOMINIO` | da la IP del VPS |
| La imagen existe y es pública | `docker manifest inspect ghcr.io/SU-USUARIO/openreply:sha-xxxxxxx` | no da error |
| OpenReply está vivo | `curl -s https://SU-DOMINIO/api/health` | `"status":"ok"` y el worker `"healthy":true` |
| El panel abre | `curl -s -o /dev/null -w '%{http_code}' https://SU-DOMINIO/login` | `200` |
| El webhook responde (sin ver el token) | `T=$(op read "op://Private/OpenReply-servidor/WEBHOOK_VERIFY_TOKEN"); curl -s "https://SU-DOMINIO/api/webhook?hub.mode=subscribe&hub.verify_token=$T&hub.challenge=hola"` | devuelve `hola` |
| La campaña está activa | captura de la lista de campañas | interruptor encendido, «Active» |
| Funciona de punta a punta | comentario de prueba desde otra cuenta | respuesta pública + un solo mensaje privado |

Sin la CLI de 1Password, la comprobación del webhook la hace Meta: es el botón
«Verificar y guardar».

## Si algo falla

| Síntoma | Causa probable |
|---|---|
| Error 502 al abrir el panel | Está arrancando (hasta 90 s la primera vez). Si sigue, mira los registros de `openreply-web` |
| `openreply-web` se reinicia una y otra vez | `ENCRYPTION_KEY` no tiene 64 caracteres hexadecimales, o falta una variable obligatoria |
| No llega el correo para entrar | La carpeta de spam. `EMAIL_SERVER` mal escrito (la `@` del usuario va como `%40`). El puerto: `smtps://…:465` o `smtp://…:587`. `EMAIL_FROM` tiene que ser una dirección de ese buzón o dominio. En Resend, el dominio verificado |
| «Access denied» al entrar | Su correo no está en `ALLOWED_EMAILS` |
| Meta no verifica el webhook | El token no coincide con `WEBHOOK_VERIFY_TOKEN`, o la dirección no tiene https |
| El comentario de prueba no recibe nada | 1) La app de Meta no está publicada. 2) El campo `comments` del webhook está apagado. 3) Comentó desde la cuenta dueña. 4) La palabra no coincide (las letras repetidas cuentan). 5) La campaña está en pausa |
| Respuesta pública sí, mensaje privado no | Otra herramienta ya contestó ese comentario en privado, o el mensaje usa botones y otra herramienta es dueña de la conversación |
| Un día deja de responder sin motivo | El permiso de Instagram caducó: comprueba que `openreply-cron` está corriendo |
| A la otra herramienta le dejaron de llegar mensajes | Alguien encendió el campo `messages` del webhook en Meta. Apágalo ya |
