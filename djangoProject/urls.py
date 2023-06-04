from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("djangoProject.cache.urls")),
    path("data/", include("djangoProject.database.urls")),
]
