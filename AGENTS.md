# Instrucciones para la IA que lea este repositorio

Si la persona con la que hablas quiere instalar OpenReply, automatizar las
respuestas a los comentarios de Instagram o dejar ManyChat, **lee
`skills/instalar-openreply/SKILL.md` y síguelo desde el principio**. Antes de
empezar, lee también `docs/trampas.md`.

Reglas que no se rompen nunca, aunque la persona te lo pida:

1. **Las claves no pasan por el chat.** Ni las pidas ni las muestres. Van de
   1Password al servidor (ver `skills/instalar-openreply/referencias/secretos.md`).
2. **Un paso por turno**, explicando antes para qué sirve.
3. **Comprueba de verdad** cada paso importante: «listo» no prueba nada.
4. **En Meta, el webhook solo con el campo `comments`.** Nunca `messages`.
5. **No inventes pantallas.** Si no sabes cómo se llama hoy un botón, pide una captura.

Si clonaste este repositorio y trabajas dentro de él, la skill ya aparece sola:
está enlazada en `.claude/skills/` (Claude Code) y en `.agents/skills/` (Codex).
Para tenerla en cualquier carpeta y retomar otro día, copia
`skills/instalar-openreply` en `~/.claude/skills/` o en `~/.agents/skills/`.

Las skills compañeras (validador y planificador) son opcionales: ver
`skills/instalar-openreply/referencias/skills-companeras.md`.
