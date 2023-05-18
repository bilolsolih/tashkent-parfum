import os  # noqa
import random
from datetime import timedelta

from django.utils import timezone
from twilio.rest import Client  # noqa

from apps.verification.models import VerificationCode


def send_code(serializer, code_type):
    phone_number = serializer.validated_data["phone_number"]
    device_id = serializer.validated_data["device_id"]
    code = random.randint(100000, 999999)
    expiration_time = timezone.now() + timedelta(minutes=2)

    VerificationCode.objects.create(
        phone_number=phone_number, device_id=device_id, code=code, expiration_time=expiration_time, code_type=code_type
    )

    # client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    print(code)

    # message = client.messages.create(
    #     body=f"Your verification code is: {code}",
    #     from_="Some twilio number which I don't have yet...",
    #     to=phone_number
    # )
