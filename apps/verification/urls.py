from django.urls import path

from . import api_endpoints as views

app_name = "verification"

urlpatterns = [
    path(
        route="verify/",
        view=views.VerificationCodeVerifyAPIView.as_view(),
        name="verification_code_verify",
    ),
]
