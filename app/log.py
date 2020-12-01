# -*- coding: utf-8 -*-
# logger.py
"""
Working logger to track settings and other information.

We'll convert to a new log config file.

"""
import logging

from environs import Env
from logdna import LogDNAHandler

logger = logging.getLogger("logdna")

logger.setLevel(logging.INFO)

env = Env()
env.read_env()

key = env("LOGDNA")

shell_handler = logging.StreamHandler()
logdna_handler = LogDNAHandler(key)

shell_handler.setLevel(logging.DEBUG)

fmt_shell = "%(levelname)s:     %(message)s"

shell_formatter = logging.Formatter(fmt_shell)

shell_handler.setFormatter(shell_formatter)


logger.addHandler(shell_handler)
logger.addHandler(logdna_handler)
