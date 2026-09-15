from django.urls import path
from .views import home, add_place


urlpatterns = [
    path('', home, name='home'),
    path('add/', add_place, name='add_place'),
]