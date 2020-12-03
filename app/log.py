# -*- coding: utf-8 -*-
# log.py
"""
Working log to track settings and other information.

We'll convert to a new log config file.

"""
import logging

import sentry_sdk
from environs import Env
from logdna import LogDNAHandler
from sentry_sdk.integrations.logging import LoggingIntegration
from timber import TimberHandler

log = logging.getLogger("logdna")

log.setLevel(logging.INFO)

env = Env()
env.read_env()

key = env("LOGDNA")
source = env("SOURCE")
timber_key = env("TIMBER")
sentry = env("DSN")


# All of this is already happening by default!
sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
)
sentry_sdk.init(
    dsn=sentry,
    integrations=[sentry_logging],
)

shell_handler = logging.StreamHandler()
logdna_handler = LogDNAHandler(key)
timber_handler = TimberHandler(
    source_id=source,
    api_key=timber_key,
)

shell_handler.setLevel(logging.DEBUG)

fmt_shell = "%(levelname)s:     %(message)s"

shell_formatter = logging.Formatter(fmt_shell)

shell_handler.setFormatter(shell_formatter)


log.addHandler(shell_handler)
log.addHandler(logdna_handler)
log.addHandler(timber_handler)
