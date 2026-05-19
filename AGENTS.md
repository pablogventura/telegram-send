# Guía para agentes

Fork **telegram-send-wait** (PyPI): envío por Telegram + `--wait-reply`. Upstream: [rahiel/telegram-send](https://github.com/rahiel/telegram-send). Detalle en [README.md](README.md).

## Stack

- **Python** ≥3.10 · **Hatchling** · `python-telegram-bot==22.5` · **uv** (`uv.lock`)
- **Licencia**: GPL-3.0-or-later

## Comandos importantes

| Acción | Comando |
|--------|---------|
| Entorno dev | `uv sync` |
| Build / publish | `uv build` · `./release.bash` |
| CLI | `telegram-send-wait` |
| Configurar | `telegram-send-wait --configure` / `--configure-group` / `--configure-channel` |
| Esperar respuesta | `telegram-send-wait "msg" --wait-reply [--timeout 300] [--reply-to-sent] [--quiet]` |
| Pruebas manuales | `./run_tests.bash` · `examples/wait_reply_example.py` |
| Publicar PyPI | [CONTRIBUTING.md](CONTRIBUTING.md) |

**Exit codes con `--wait-reply`:** `0` = respuesta en stdout · `2` = timeout · `1` = config/red.

## Estructura

```
telegram_send/
  telegram_send.py   # CLI, send, wait_for_reply, configure, migrate global config
  utils.py
  version.py         # 1.0.0
```

## API pública (`__all__`)

`configure`, `delete`, `send`, `wait_for_reply`, `WaitReplyTimeout`, `__version__`

## Config

- Usuario: `user_config_dir("telegram-send")` (compatible con upstream)
- Global `-g`: `/etc/telegram-send-wait.conf` (migra desde `/etc/telegram-send.conf` si existe)

## Qué NO hacer

- Instalar junto con el paquete PyPI `telegram-send` en el mismo venv
- Commitear `*.conf`, tokens, artefactos de prueba
- Refactors masivos; `--wait-reply` solo con texto (no archivos/medios en la misma invocación)
- Asumir tests automáticos (solo smoke manual)
