# Fase 2 · Las claves, en 1Password

**La regla:** ninguna clave pasa por este chat. Ni la pides, ni la muestras, ni
la escribes en un archivo del repo. Explícale por qué en una frase: «lo que se
escribe en un chat queda guardado en sitios que no controlas, y una captura de
pantalla puede acabar en cualquier parte».

## El elemento de 1Password

Pídele que cree en 1Password un elemento nuevo de tipo **Servidor** (o «Nota
segura») llamado exactamente **`OpenReply-servidor`**, sin espacios (así se
puede leer desde la terminal), en su bóveda personal. Tendrá estos campos, de
tipo contraseña:

| Campo | Cómo se genera |
|---|---|
| `NEXTAUTH_SECRET` | aleatorio, 48 caracteres hexadecimales |
| `CRON_SECRET` | igual |
| `POSTGRES_PASSWORD` | igual |
| `WEBHOOK_VERIFY_TOKEN` | igual |
| `ENCRYPTION_KEY` | aleatorio, **64** caracteres hexadecimales (OpenReply lo exige así) |
| `INSTAGRAM_APP_ID`, `INSTAGRAM_APP_SECRET`, `FACEBOOK_APP_SECRET` | los copia ella de Meta en la Fase 4 |
| `EMAIL_SERVER` (buzón propio) o `RESEND_API_KEY` | ver «El correo», abajo |
| `HOSTINGER_API_TOKEN` | solo si despliega por la API (Fase 5) |

Solo letras y números: un `$`, un espacio o una comilla rompen la conexión con
la base de datos sin un error claro.

## Cómo generar sin verlas

**Con la CLI de 1Password (`op`).** Tú ejecutas esto. Las claves se generan y
se guardan sin pasar por la pantalla:

```bash
op item create --category server --title OpenReply-servidor \
  "NEXTAUTH_SECRET[password]=$(openssl rand -hex 24)" \
  "CRON_SECRET[password]=$(openssl rand -hex 24)" \
  "POSTGRES_PASSWORD[password]=$(openssl rand -hex 24)" \
  "WEBHOOK_VERIFY_TOKEN[password]=$(openssl rand -hex 24)" \
  "ENCRYPTION_KEY[password]=$(openssl rand -hex 32)" > /dev/null && echo "creado"
```

Comprueba el formato sin mostrar el valor:

```bash
op read "op://Private/OpenReply-servidor/ENCRYPTION_KEY" | grep -qE '^[0-9a-f]{64}$' && echo "ENCRYPTION_KEY bien"
```

(Si su bóveda no se llama `Private`, usa la que te diga.)

**Sin la CLI.** Campo por campo: tú generas el valor directamente en su
portapapeles, sin que salga en pantalla, y ella lo pega en 1Password.

- Mac: `openssl rand -hex 24 | tr -d '\n' | pbcopy`
- Linux: `openssl rand -hex 24 | tr -d '\n' | wl-copy` (o `xclip -selection clipboard`)
- Windows (PowerShell):
  `$b=New-Object byte[] 24; [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($b); (($b|%{$_.ToString('x2')}) -join '') | Set-Clipboard`

Para `ENCRYPTION_KEY`, 32 en vez de 24. Después de pegar cada uno, que diga
«listo» y vas al siguiente.

## El correo (`EMAIL_SERVER`)

Si eligió un buzón propio, el campo `EMAIL_SERVER` es una sola línea que
lleva dentro la contraseña del buzón. Cárgale en el portapapeles la plantilla,
con sus datos reales salvo la contraseña:

`smtps://panel%40tudominio.com:CONTRASENA@smtp.tuproveedor.com:465`

Ella la pega en el campo de 1Password y cambia ahí mismo `CONTRASENA` por la
de su buzón. La `@` del usuario va escrita `%40`. Si la contraseña del buzón
tiene símbolos, mejor que le ponga una nueva solo con letras y números: los
símbolos rompen esa línea.

## Si te pega una clave en el chat

Sin dramatismo: «Gracias por la confianza, pero esa clave ya no es segura
porque quedó escrita aquí. Vamos a generar otra». Y la regeneráis.
