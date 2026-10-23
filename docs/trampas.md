# Trampas que nadie te cuenta

Todo esto salió de una instalación real que hoy está en producción. La guía de
OpenReply no lo dice, o dice lo contrario. Cada punto es una tarde perdida que
te puedes ahorrar.

## Meta (la app de desarrollador)

1. **Meta se hace en dos mitades.** Al principio creas la app y sacas las
   claves. Al final, con tu panel ya funcionando en internet, conectas el
   webhook y publicas la app, porque publicar exige que tus direcciones existan.
2. **Al verificar el webhook, Meta enciende casi todos los campos.** Apágalos
   todos menos `comments` y revisa la lista dos veces: es fácil que se quede
   uno encendido.
3. **Mientras la app no esté publicada (Live), los comentarios reales no
   llegan.** Solo funciona el botón de prueba de Meta.
4. **La invitación de tester no aparece en la app de Instagram.** Se acepta en
   la web: instagram.com/accounts/manage_access.
5. **Tus propios comentarios no cuentan.** OpenReply ignora a la cuenta dueña:
   las pruebas se hacen desde otra cuenta de Instagram.
6. **Tu Instagram tiene que ser profesional** (Empresa o Creador).

## Si ya usas otra herramienta para los mensajes (ManyChat, Superchat…)

7. **Nunca enciendas el campo `messages`** en el webhook de Meta, ni actives
   «Take control of conversations». Le quitarías los mensajes a tu otra
   herramienta. OpenReply solo necesita `comments`.
8. **Los botones fallan** cuando otra herramienta es la dueña de la
   conversación (error «not the thread owner»). Pon los enlaces escritos dentro
   del texto del mensaje y no uses «+ Add A Link».
9. **Por lo mismo, nada de «opening DM», «follow requirement» ni «follow-up».**
   Todos usan botones o mensajes de más.
10. **Si tu otra herramienta también contesta comentarios, decide quién
    contesta cada palabra.** Si contestan las dos, la persona recibe dos
    mensajes.

## Las campañas

11. **Instagram permite UNA respuesta privada por comentario.** Si un comentario
    activa dos campañas, solo una consigue mandar el mensaje. Las respuestas
    públicas, en cambio, salen todas.
12. **OpenReply no repite por comentario, pero sí por persona.** Quien comenta
    la palabra en cinco publicaciones recibe cinco mensajes.
13. **Máximo 10 palabras por campaña.** Las mayúsculas, las tildes y los signos
    no importan («Proyecto!!» entra). Las letras repetidas sí («proyectoooo» no
    entra). Gasta las 10 en las faltas típicas.
14. **«any word» responde a TODOS los comentarios**, haters incluidos. Úsalo
    solo si de verdad quieres eso.
15. **Duplicar una campaña la crea en pausa, pero guardarla puede activarla.**
    Revisa el interruptor después de guardar.
16. **El panel no manda las invitaciones por correo.** Genera un enlace
    `/invite/...` que tienes que enviar tú.

## El servidor

17. **No construyas la imagen en un servidor pequeño.** El build se come toda
    la CPU durante minutos. Constrúyela en GitHub (plantillas/publicar-imagen.yml).
18. **Sin el servicio `cron`, el permiso de Instagram caduca en silencio.** Un
    día deja de responder y nadie sabe por qué.
19. **Sin `ALLOWED_EMAILS`, cualquiera que llegue a tu panel se crea su propio
    espacio.**
20. **Redis con `noeviction`.** Si Redis borra claves para hacer sitio, se
    pierden mensajes de la cola.
21. **Las claves solo con letras y números.** Un `$`, un espacio o una comilla
    en la contraseña de la base de datos rompen la conexión sin un error claro.
22. **Las claves nunca en un chat**, tampoco en el de tu IA. Van del gestor de
    contraseñas al archivo `.env` del servidor, y de ahí no salen.

## Para tu IA

23. **En Mac, copiar al portapapeles con acentos o emojis** necesita
    `LANG=en_US.UTF-8 pbcopy`. Sin eso llegan rotos («¬°Te lo mand√©…»).
24. **«Ya lo guardé» no prueba nada.** Después de cada paso importante, la IA
    comprueba de verdad: la dirección responde, la campaña está activa, el
    comentario de prueba recibió su mensaje.
