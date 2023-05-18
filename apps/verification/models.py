from django.db import models

from apps.common.models import BaseModel


class VerificationCode(BaseModel):
    class CodeTypes(models.TextChoices):
        VER = ("ver", "Verification")
        RES = ("res", "Password Reset")

    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()
    device_id = models.CharField(max_length=50)
    type = models.CharField(choices=CodeTypes.choices, max_length=3, default="ver")

    class Meta:
        verbose_name = "Verification code"
        verbose_name_plural = "Verification codes"
        unique_together = ["phone_number", "code", "type", "device_id"]

    def __str__(self):
        return f"Verification code for {self.phone_number}, device {self.device_id}"
