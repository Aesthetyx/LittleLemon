from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("menu", views.MenuView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="singleMenuItem")
]