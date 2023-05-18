from os import getenv

from .base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": getenv("DB_ENGINE"),
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    }
}

DEBUG = False

ADMINS = [("BlackHoler", "BilolMuhammadSolih@gmail.com")]
