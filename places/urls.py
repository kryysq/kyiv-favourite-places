from django.urls import path
from .views import (home, add_place, login_view, logout_view, register, place_detail)


urlpatterns = [
    path('', home, name='home'),
    path('add/', add_place, name='add_place'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('place/<int:place_id>/', place_detail, name='place_detail'),
]