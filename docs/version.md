# Versión probada

OpenReply cambia rápido. Esta guía está probada con una versión concreta, y tu
instalación tiene que usar esa misma.

| Pieza | Versión |
|---|---|
| OpenReply (github.com/diwenne/openreply) | commit `dca8713` (21-oct-2026) |
| Postgres | `postgres:16-alpine` |
| Redis | `redis:7-alpine` |
| Caddy | `caddy:2.8.4-alpine` |
| API de Meta | `v25.0` |

## Cómo se usa la versión fijada

En tu copia (fork) de OpenReply se crea la rama `instalacion` a partir del
commit `dca8713`, y ahí se añade `plantillas/publicar-imagen.yml`. GitHub
construye la imagen de esa versión exacta.

## Cómo se actualiza

1. Alguien prueba la guía entera contra una versión nueva de OpenReply.
2. Si todo funciona, cambia el commit de esta tabla y la fecha.
3. Quien ya tenga OpenReply instalado mueve su rama `instalacion` a ese commit,
   espera la imagen nueva y cambia `OPENREPLY_IMAGE` en su `.env`.

Nunca se actualiza sin probar: una versión nueva puede cambiar los nombres de
las variables o los pasos de Meta.
