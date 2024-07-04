from django.urls import path
from . views import HomeView, PagesDetailView
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home-page"),
    path("page", PagesDetailView.as_view(), name="page"),
    path("contacts/", views.contacts, name="contacts"),
]