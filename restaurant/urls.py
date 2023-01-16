from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("menu", views.MenuView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="singleMenuItem"),
    path("api-token-auth", obtain_auth_token),
]