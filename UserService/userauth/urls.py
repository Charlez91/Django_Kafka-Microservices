from django.urls import path

from userauth.views import RegisterView

urlpatterns = [
    path("register/", view=RegisterView.as_view(), name="auth_register")
]