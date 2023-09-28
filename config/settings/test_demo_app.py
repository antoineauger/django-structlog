"""
With these settings, tests run faster.
"""

# noinspection PyUnresolvedReferences
from .base import *  # noqa: F401,F403

# noinspection PyUnresolvedReferences
from .test import DATABASES, LOGGING  # noqa: F401

DJANGO_STRUCTLOG_COMMAND_LOGGING_ENABLED = True

IS_WORKER = False
