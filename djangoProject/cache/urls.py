from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes, name="routes"),
    path("cache/", views.cache_get, name="cache_get"),
    path("cache/put/", views.cache_put, name="cache_put"),
]
