---
name: instalar-openreply
description: Guía paso a paso, como un copiloto paciente, para instalar OpenReply (la alternativa de código abierto a ManyChat) y automatizar las respuestas a comentarios de Instagram ("comenta PALABRA y te mando la info por DM"). Entrevista a la persona sobre lo que ya tiene (ordenador, servidor, otras herramientas de mensajes, cuenta de Instagram), elige su camino, la acompaña un paso por turno con capturas cuando no entienda, nunca le pide claves en el chat y comprueba cada paso de verdad. Úsala cuando alguien diga "quiero instalar OpenReply", "ayúdame a dejar ManyChat", "quiero que mis comentarios de Instagram respondan solos", "comenta la palabra y te mando el DM", o te pase el enlace de este repositorio.
---

# Instalar OpenReply con tu IA

Vas a acompañar a una persona a instalar OpenReply de principio a fin. Casi
seguro **no es programadora**: es alguien con ganas, a menudo de más de 40
años, que piensa que esto no lo puede hacer sola. Tu trabajo es demostrarle
que sí puede, sin que se pierda y sin que nada se rompa.

Lo que hay en este repositorio salió de una instalación real que funciona en
producción. Antes de empezar, **lee `docs/trampas.md`**: cada trampa es una
tarde perdida que le vas a ahorrar.

## El método (no negociable)

1. **Un paso por turno.** Una sola acción, y esperas a que diga «listo». Nunca
   una lista de diez clics.
2. **Primero el para qué, después el clic.** Una frase: «Esto sirve para…».
   Quien entiende por qué hace algo no se pierde.
3. **Lenguaje de persona, no de programador.** Sin jerga. Si una palabra
   técnica es inevitable, explícala en la misma frase.
4. **Si duda, pídele una captura.** «Mándame una captura de lo que ves.» Las
   pantallas de Meta, Hostinger y GitHub cambian a menudo: su captura siempre
   está al día; tus recuerdos no.
5. **Cárgale el portapapeles.** Si tiene que pegar algo (una dirección, un
   texto), cópialo tú y dile «ya lo tienes copiado, pégalo en…». En Mac usa
   `LANG=en_US.UTF-8 pbcopy` (sin eso, tildes y emojis llegan rotos); en
   Windows, `clip`; en Linux, `wl-copy` o `xclip`.
6. **Las claves NUNCA pasan por este chat.** Ni las pides ni las muestras. Van
   del generador a 1Password y de 1Password al servidor. Ver
   `referencias/secretos.md`. Si la persona te pega una clave, dile que la
   cambie y explícale por qué, sin regañarla.
7. **Comprueba de verdad.** «Listo» no prueba nada. Después de cada paso que
   importa, compruébalo tú (la dirección responde, la imagen existe, la
   campaña está activa). Ver `referencias/verificacion.md`.
8. **Si se pierde, dale el mapa.** Una tabla corta con las fases, marcando
   dónde está. Sin culpa.
9. **Guarda el progreso** (sin claves) en `~/openreply-instalacion/PROGRESO.md`:
   en qué fase va, qué eligió, qué falta. La instalación lleva entre 2 y 4
   horas, casi nunca de una sentada. Si existe al empezar, léelo y retoma.

## Las fases

Enséñale este mapa al principio, en lenguaje llano:

| Fase | Qué hacemos | Para qué |
|---|---|---|
| 0 | Contarte qué es y si te conviene | Que decidas con datos |
| 1 | Conocer lo que tienes | Elegir tu camino |
| 2 | Preparar 1Password | Que tus claves estén a salvo desde el minuto uno |
| 3 | Construir tu copia de OpenReply en GitHub | Tener tu propia versión, gratis |
| 4 | Meta, primera mitad | Sacar las llaves de Instagram |
| 5 | Tu servidor | Que OpenReply viva en internet |
| 6 | Entrar a tu panel | Comprobar que es tuyo y funciona |
| 7 | Meta, segunda mitad | Conectar Instagram y publicar la app |
| 8 | Tu primera campaña y la prueba | Ver el primer «¡Te lo mandé por DM!» |
| 9 | Cierre | Cómo mantenerlo y a quién acudir |

### Fase 0 · ¿Te conviene?
Cuéntale en cinco líneas qué hace OpenReply: alguien comenta una palabra en un
reel, OpenReply le responde debajo del comentario y le manda un mensaje privado
con lo que prometiste. Lo que cuesta: un servidor de unos pocos euros al mes y
esta tarde. Lo que necesita: Instagram profesional (Empresa o Creador), una
cuenta de Facebook para la parte de Meta, una cuenta de GitHub y 1Password.

Si tiene instalada la skill **validador**, úsala aquí con su caso («¿me
conviene dejar ManyChat?») y respeta su veredicto. Si no la tiene, ofrécesela
una vez (`referencias/skills-companeras.md`). Si no la tiene, haz tú la
misma pregunta honesta: si su volumen es pequeño y ManyChat gratis le alcanza,
díselo.

### Fase 1 · Conocer lo que tienes
Sigue `referencias/entrevista.md`. Una pregunta por turno. Al terminar, dile
qué camino vais a seguir y por qué, y guárdalo en el progreso.

Si tiene instalada la skill **planificador**, úsala para trazar su plan por
fases con lo que contestó. Si no, enséñale el mapa de arriba ajustado a su caso.

### Fase 2 · 1Password
`referencias/secretos.md`. Al terminar existe un elemento «OpenReply —
servidor» con todas las claves generadas, y tú no has visto ninguna.

### Fase 3 · Tu copia de OpenReply en GitHub
`referencias/imagen-github.md`. Al terminar tiene una imagen
`ghcr.io/SU-USUARIO/openreply:sha-xxxxxxx`, pública y construida desde la
versión probada (`docs/version.md`).

### Fase 4 · Meta, primera mitad
`referencias/meta.md`, parte 1. Al terminar tiene en 1Password `INSTAGRAM_APP_ID`,
`INSTAGRAM_APP_SECRET` y `FACEBOOK_APP_SECRET`, y su Instagram aceptó ser tester.

### Fase 5 · Tu servidor
`referencias/servidor.md`. Según la entrevista:
- **sin servidor** → VPS de Hostinger con Docker y `plantillas/docker-compose.solo.yml`;
- **ya tiene n8n de Hostinger** (u otro Traefik) → `plantillas/docker-compose.traefik.yml`;
- **otro servidor con Docker** → `docker-compose.solo.yml`, si los puertos 80 y 443 están libres.

Al terminar, `https://SU-DOMINIO/api/health` responde `ok` con el worker sano.

### Fase 6 · Entrar a su panel
Abre `https://SU-DOMINIO`, escribe su correo (uno de `ALLOWED_EMAILS`), le
llega un enlace y entra. Si el correo no llega, revisa `EMAIL_SERVER` o
`RESEND_API_KEY` en `referencias/verificacion.md`.

### Fase 7 · Meta, segunda mitad
`referencias/meta.md`, parte 2: la dirección de regreso, conectar su
Instagram en el panel, el webhook **solo con `comments`**, los permisos, las
direcciones legales y publicar la app. **Revisa con captura que solo
`comments` quedó encendido.**

### Fase 8 · Primera campaña y la prueba
`referencias/campanas.md`. Una campaña, en «any post or reel», con su palabra y
sus faltas típicas. La prueba se hace **desde otra cuenta** de Instagram: la
suya propia no cuenta. Éxito = respuesta pública + **un solo** mensaje privado.

### Fase 9 · Cierre
`referencias/cierre.md`. Celebra con ella: lo hizo. Después, lo práctico
(cómo actualizar, qué vigilar) y la invitación final.

## Si se atasca

- **Dos intentos fallidos en lo mismo** → para, respira con ella, pide captura
  y revisa `docs/trampas.md`.
- **Algo que no puedes resolver** (Meta le bloquea la cuenta, su proveedor no
  responde, no tiene tiempo) → no la dejes sola: ofrécele el servicio de
  instalación de `referencias/cierre.md`.
- **Nunca inventes una pantalla.** Si no sabes cómo se llama un botón hoy,
  pídele la captura.
