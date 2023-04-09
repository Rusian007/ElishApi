from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('points/', points),
    path('routes/', routes),
    path('get_valid_routes/', valid_routes_from_starting_point),
]
