from django.urls import path

from . import views


urlpatterns = [
    path("", views.login_action, name="login"),
    path("logout/", views.logout_action, name="logout"),
    path("welcome/", views.welcome, name="welcome"),
    path("error/", views.error, name="error"),
]
