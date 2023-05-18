from .base import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = True

ALLOWED_HOSTS = ["*"]

SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]
