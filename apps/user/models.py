from typing import List  # noqa F401

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(verbose_name=_("Phone number"), max_length=15, unique=True)
    full_name = models.CharField(verbose_name=_("Fullname"), max_length=128)

    email = models.EmailField(verbose_name=_("Email address"), blank=True, null=True)
    is_staff = models.BooleanField(
        verbose_name=_("Staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Is active?"),
        default=False,
        help_text=_("Designates whether this user should be treated as active." "Unselect this instead of deleting accounts."),
    )
    is_verified = models.BooleanField(verbose_name=_("Is user phone number verified?"), default=False)
    is_deleted = models.BooleanField(verbose_name=_("Is user deleted?"), default=False)
    allowed_to_reset = models.BooleanField(verbose_name=_("Is user allowed to reset password?"), default=False)
    date_joined = models.DateTimeField(verbose_name=_("Date joined"), default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
