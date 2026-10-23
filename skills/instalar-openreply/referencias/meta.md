# Fases 4 y 7 · Meta, en dos mitades

**Para qué:** Instagram solo deja que una herramienta conteste comentarios si
tiene una «app» registrada en Meta. Se hace en dos mitades porque la segunda
necesita que su panel ya esté en internet.

Las pantallas de Meta cambian a menudo, y los nombres pueden salirle en inglés
o en español. **Ante cualquier duda, captura.** Aquí va lo que hay que
conseguir en cada paso, no el texto exacto de cada botón.

## Primera mitad (Fase 4, antes del servidor)

1. **developers.facebook.com**, con su cuenta de Facebook → **Mis apps → Crear app**.
2. Nombre de la app (por ejemplo, «OpenReply» y su marca) y su correo de contacto.
3. Caso de uso: **Administrar mensajes y contenido en Instagram** («Manage
   messaging & content on Instagram»).
4. Portfolio de negocio: **«Aún no quiero conectar un portfolio comercial»**.
   Se puede vincular después.
5. Requisitos, resumen y **Crear app**. Si Meta le pide su contraseña de
   Facebook, la escribe ella, no tú.
6. Dentro del caso de uso, en la configuración de la API con inicio de sesión
   de Instagram, que copie **directamente a 1Password** (nunca al chat):
   - el **ID de la app de Instagram** → `INSTAGRAM_APP_ID`;
   - la **clave secreta de la app de Instagram** → `INSTAGRAM_APP_SECRET`.
7. **Configuración de la app → Básica → Clave secreta de la app** → a
   1Password como `FACEBOOK_APP_SECRET`.
8. **Roles de la app → Añadir tester de Instagram** con su usuario de
   Instagram. La invitación **no aparece en la app de Instagram**: se acepta
   en la web, **instagram.com/accounts/manage_access** → «Invitaciones de tester».

## Segunda mitad (Fase 7, con el panel ya funcionando)

Cárgale en el portapapeles cada dirección, con su dominio real.

1. **La dirección de regreso.** En la configuración del inicio de sesión de
   Instagram, en las URI de redirección de OAuth, añade
   `https://SU-DOMINIO/api/instagram/callback` y guarda.
2. **Conectar su Instagram.** En su panel de OpenReply → **Settings** → conectar
   cuenta de Instagram → entra con Instagram y acepta los permisos.
3. **El webhook.** En la configuración de webhooks del caso de uso:
   - URL de devolución: `https://SU-DOMINIO/api/webhook`;
   - token de verificación: el `WEBHOOK_VERIFY_TOKEN`. Lo copia ella de 1Password;
   - **Verificar y guardar**.
4. **🔴 Los campos del webhook.** Al verificar, Meta enciende casi todos.
   **Apágalos todos menos `comments`.** Pídele una captura de la lista final y
   compruébala tú: es fácil que se quede uno encendido, y si es `messages`, a
   quien use otra herramienta le quita los mensajes.
5. **Los permisos.** En el caso de uso → **Personalizar**: deben estar
   `instagram_business_basic`, `instagram_business_manage_comments` e
   `instagram_business_manage_messages`. Este último hace falta para mandar el
   mensaje privado, y **no es lo mismo que el campo `messages` del webhook**,
   que sigue apagado.
6. **Las direcciones legales.** Configuración → Básica:
   - Política de privacidad: `https://SU-DOMINIO/privacy`;
   - Condiciones del servicio: `https://SU-DOMINIO/terms`;
   - Eliminación de datos: `https://SU-DOMINIO/data-deletion`;
   - la categoría, y guardar.
7. **Publicar la app** (modo «Live» / «Publicada»). Mientras no esté
   publicada, **los comentarios reales no llegan**: solo el botón de prueba de
   Meta. El acceso estándar basta para su propia cuenta.

## Comprobaciones

- El panel muestra su Instagram conectado.
- La captura de los campos del webhook: **solo `comments`**.
- La app sale como publicada.
- En el panel, **Diagnostics** solo muestra fallos: que esté vacío es buena señal.
