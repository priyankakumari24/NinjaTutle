from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact/", views.contact, name='contact'),
    path("login/", views.login, name='login'),
    path("external/", views.external, name='external')
]
