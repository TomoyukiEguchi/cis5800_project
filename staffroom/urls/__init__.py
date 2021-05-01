from django.urls import path, include
from ..views import StaffroomTemplateView, Login, Logout, SignUp


app_name = "staffroom"

urlpatterns = [
    path("", StaffroomTemplateView.as_view(), name="index"),
    path("login", Login.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
    path("signup", SignUp.as_view(), name="signup"),
    path("restaurant/", include("staffroom.urls.restaurant", namespace="restaurant")),
]