# respondedor

> Tu propio «comenta la palabra y te mando la info por DM» en Instagram, instalado con tu IA. Sin pagar ManyChat.

**Primera versión (octubre de 2026).** Funciona en producción en mi negocio. Si algo de la guía no te cuadra, abre un *issue*: lo corrijo rápido.

> **¿Eres una IA y te pasaron este enlace?** Lee `AGENTS.md` y sigue
> `skills/instalar-openreply/SKILL.md`.

## Qué consigues

Alguien comenta tu palabra en un reel («PROYECTO», «INFO», la que quieras) y, en segundos:

1. le respondes debajo del comentario («¡Te lo mandé por DM! 📩»);
2. le llega un mensaje privado con lo que le prometiste.

En todas tus publicaciones, las 24 horas. Funciona con [OpenReply](https://github.com/diwenne/openreply), una alternativa a ManyChat de código abierto: no pagas por contacto.

## Por qué existe

En redes venden OpenReply como magia: «instálalo y listo». Hay trabajo detrás. Lo instalé para mi negocio, me encontré con cada trampa de Meta y del servidor, y convertí todo eso en un copiloto. **Tu IA te pregunta lo que tienes y te lleva de la mano, un paso cada vez.**

No hace falta saber programar. Sí hace falta tener ganas y una tarde.

## Lo que necesitas

- **Claude Code o Codex**, la IA que te va a guiar.
- **Un Instagram profesional** (Empresa o Creador).
- **Una cuenta de Facebook**, para la parte de Meta.
- **Una cuenta de GitHub**, gratis.
- **1Password**, para que tus claves nunca anden sueltas.
- **Un servidor.** Si no tienes, un VPS pequeño de Hostinger cuesta unos pocos euros al mes: [hostinger.com](https://www.hostinger.com/es?REFERRALCODE=GQAHJSOLIIPU). Es mi enlace de afiliado: si contratas con él recibo una comisión, y a ti no te cuesta más.
- **Entre 2 y 4 horas.** Se puede hacer en dos días: tu IA guarda por dónde vas.

## Cómo empezar

Copia esto y pégaselo a tu IA:

```
Clona https://github.com/hildemarosolis/respondedor, lee su AGENTS.md y ayúdame a instalar OpenReply para que mis comentarios de Instagram se respondan solos.
```

Te hará unas preguntas y te llevará paso a paso. **Nunca te pedirá tus claves por el chat.** Si alguna vez lo hace, no se las des.

## Qué hay dentro

| Carpeta | Qué es |
|---|---|
| `skills/instalar-openreply/` | La skill que convierte a tu IA en tu copiloto de instalación |
| `docs/trampas.md` | Las 24 trampas que encontré: léelas antes de tocar Meta |
| `docs/version.md` | La versión de OpenReply con la que está probada la guía |
| `plantillas/` | Lo que va a tu servidor (con un servidor vacío, o con n8n de Hostinger) |
| `herramientas/` | El despliegue automático a Hostinger (lee las claves de 1Password sin mostrarlas) y el guardián que impide publicar datos privados |

Por el camino, tu IA te ofrecerá dos skills mías, gratis: [validador](https://github.com/hildemarosolis/validador), para decidir si te conviene, y [planificador](https://github.com/hildemarosolis/planificador), para ordenar el trabajo.

## Si te atascas

¿Te atascaste en algún paso, o prefieres que te lo dejen funcionando? El equipo de **VisionCoder** te lo instala. Escríbeles a **hola@visioncoder.app**.

## Créditos

- [OpenReply](https://github.com/diwenne/openreply) es de su autor, con licencia MIT. Esta guía no es oficial.
- La guía es mía, también MIT: [Hildemaro Solís](https://github.com/hildemarosolis). Construyo con IA y lo cuento tal cual, en GitHub y en Instagram ([@hildemarosolis](https://www.instagram.com/hildemarosolis/)).
