# Fase 1 · La entrevista

Una pregunta por turno, con su «para qué». Guarda cada respuesta en
`~/openreply-instalacion/PROGRESO.md` (nunca una clave). Si no sabe contestar
algo, pídele una captura y averígualo tú.

| # | Pregunta | Para qué / qué cambia |
|---|---|---|
| 1 | ¿Usas Mac, Windows o Linux? | Cómo le cargas el portapapeles y qué comandos usas |
| 2 | ¿Tu Instagram es profesional (Empresa o Creador)? | Es obligatorio. Si no, se cambia antes de seguir: Instagram → Configuración → Tipo de cuenta y herramientas |
| 3 | ¿Ya usas alguna herramienta que responde mensajes o comentarios de Instagram? (ManyChat, Superchat, Respond.io, Kommo…) | Si sí: **modo convivencia** (solo `comments`, nada de botones; ver `docs/trampas.md` 7 a 10). Si usa ManyChat y quiere dejarlo: se apagan sus automatizaciones de esas palabras **después** de comprobar que OpenReply funciona, no antes |
| 4 | ¿Tienes un servidor? | Ninguno → VPS de Hostinger. Hostinger con n8n → `docker-compose.traefik.yml`. Otro servidor con Docker → `docker-compose.solo.yml`. «No sé» → pídele captura de su panel de hosting |
| 5 | ¿Tienes un dominio propio? | No hace falta: un VPS de Hostinger trae una dirección que funciona sin tocar nada. Si quiere el suyo, añade un registro DNS |
| 6 | ¿Tienes cuenta de GitHub? | Ahí se construye su copia de OpenReply, gratis. Si no tiene, se crea en github.com |
| 7 | ¿Tienes 1Password? ¿Y su app de escritorio con la opción «Integrar con la CLI de 1Password»? | 1Password es obligatorio (claves a salvo). La CLI (`op`) es opcional: con ella generas y despliegas sin que nadie vea nada, sin copiar y pegar claves |
| 8 | ¿Desde qué buzón quieres que salgan los enlaces para entrar a tu panel? | Explícalo así: «el panel no usa contraseña; te manda un enlace por correo cada vez que entras. Ese correo lo envía un buzón, el cartero». Opciones: un buzón de su dominio (SMTP, mejor uno dedicado como panel@) o Resend. **Su Gmail personal, mejor no**: la «contraseña de aplicación» se salta su verificación en dos pasos |
| 9 | ¿Quién más entrará al panel? | Los correos de `ALLOWED_EMAILS`. Nadie más puede entrar |
| 10 | ¿Qué palabra quieres que comenten y qué les mandas? | La primera campaña. Puede decidirlo al final |

Al terminar, resúmele su camino en tres líneas («Vas a usar un VPS de
Hostinger, tu copia de OpenReply en GitHub y 1Password. Como ya usas ManyChat,
OpenReply solo escuchará comentarios.») y pregúntale si está de acuerdo.
