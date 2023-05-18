from django.urls import path

from . import api_endpoints as views

app_name = "users"

urlpatterns = [
    path("register/", views.UserInitialRegisterAPIView.as_view(), name="user_register"),
    path("set_password/", views.UserSetPasswordAPIView.as_view(), name="user_set_password"),
    path("reset_password/send/", views.UserResetPasswordSendCodeAPIView.as_view(),
         name="user_reset_password_send_code"),
    path("reset_password/reset/", views.UserResetPasswordAPIView.as_view(), name="user_reset_password_reset"),
    path("update/<int:pk>/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("login/", views.LoginAPIView.as_view(), name="user_login"),
    path("logout/", views.LogoutAPIView.as_view(), name="user_logout"),
    path("all-users/", views.UserListAPIView.as_view(), name="user_list"),
    path("all-users/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_detail"),
    path("delete-user/<int:pk>/", views.UserDestroyAPIView.as_view(), name="user_delete"),
]
