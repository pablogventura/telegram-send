"""
.. include:: ../README.md
"""
from .version import __version__
from .telegram_send import (
    WaitReplyTimeout,
    configure,
    delete,
    send,
    wait_for_reply,
)


__all__ = [
    "WaitReplyTimeout",
    "configure",
    "delete",
    "send",
    "wait_for_reply",
    "__version__",
]
