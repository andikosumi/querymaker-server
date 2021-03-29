from django.urls import path

from .views import creation_view

urlpatterns = [
    path('', creation_view, name='creation')
]