import logging
import os
import sys

from .base import *  # noqa: F401, F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cc4i1wju9th3h0y-x@*u$c#%s%+7it)#0u3te_nt@)@l2u^m44'

DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        'all': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "message:%(message)s",
                "process:%(process)d",
                "thread:%(thread)d",
            ])
        },
        'verbose': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "asctime:%(asctime)s",
                "module:%(module)s",
                "name:%(name)s",
                "lineno:%(lineno)d",
                "funcName:%(funcName)s",
                "message:%(message)s",
            ])
        },
        # "django.server": {
        #     "()": "django.utils.log.ServerFormatter",
        #     "format": "[%(server_time)s] %(message)s",
        # },
    },
    "handlers": {
        "file": {
            'formatter': 'verbose',
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
        "console": {
            "formatter": "verbose",
            'level': 'DEBUG',
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.server": {
            "handlers": ["console"],
            "level": "DEBUG",
        },

        "root": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}
