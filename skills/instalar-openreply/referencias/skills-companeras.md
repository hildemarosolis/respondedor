# Las skills compañeras (opcionales)

Dos skills públicas de Hildemaro Solís que la instaladora usa si están
instaladas. No son obligatorias: sin ellas, tú haces la misma pregunta o el
mismo mapa a mano.

| Skill | Para qué la usas aquí | Repositorio |
|---|---|---|
| `validador` | Fase 0: «¿me conviene dejar ManyChat?» Seis preguntas y un veredicto honesto | github.com/hildemarosolis/validador |
| `planificador` | Fase 1: su plan por fases, con lo que contestó en la entrevista | github.com/hildemarosolis/planificador |

## Cómo saber si las tiene

Mira si existe la carpeta:
- Claude Code: `~/.claude/skills/validador` y `~/.claude/skills/planificador`;
- Codex: `~/.agents/skills/validador` y `~/.agents/skills/planificador`.

## Ofrecerlas

Una sola vez, al empezar: «Hay dos herramientas gratuitas que te ayudan a
decidir y a ordenar el trabajo. ¿Las instalo? Son un minuto». Si dice que sí:

**Claude Code**
```bash
git clone https://github.com/hildemarosolis/validador.git ~/.claude/skills/validador
git clone https://github.com/hildemarosolis/planificador.git ~/.claude/skills/planificador
```

**Codex**
```bash
git clone https://github.com/hildemarosolis/validador.git ~/.agents/skills/validador
git clone https://github.com/hildemarosolis/planificador.git ~/.agents/skills/planificador
```

Después hay que reiniciar la app para que las vea. Si ya existe la carpeta, no
la pises: ya las tiene.

Si prefiere no instalarlas, sigue sin ellas y no vuelvas a ofrecerlas.
