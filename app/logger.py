# -*- coding: utf-8 -*-
# logger.py
"""
Working logger to track settings and other information.

We'll convert to a new log config file.

"""

import logging

import timber
from environs import Env
from rich.logging import RichHandler

log = logging.getLogger(__name__)

env = Env()
env.read_env()


shell_handler = RichHandler()
timber_handler = timber.TimberHandler(
    source_id=env("SOURCE"),
    api_key=env("TIMBER"),
    drop_extra_events=False,
)

log.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.DEBUG)


fmt_shell = "%(message)s"


shell_formatter = logging.Formatter(fmt_shell)

shell_handler.setFormatter(shell_formatter)

log.addHandler(shell_handler)
log.addHandler(timber_handler)
