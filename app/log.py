# -*- coding: utf-8 -*-
# log.py
"""
Working log to track settings and other information.

We'll convert to a new log config file.

"""
import logging

from environs import Env
from logdna import LogDNAHandler

log = logging.getLogger("logdna")

log.setLevel(logging.INFO)

env = Env()
env.read_env()

key = env("LOGDNA")

shell_handler = logging.StreamHandler()
logdna_handler = LogDNAHandler(key)

shell_handler.setLevel(logging.DEBUG)

fmt_shell = "%(levelname)s:     %(message)s"

shell_formatter = logging.Formatter(fmt_shell)

shell_handler.setFormatter(shell_formatter)


log.addHandler(shell_handler)
log.addHandler(logdna_handler)
