from django.apps import AppConfig
from .utils import get_db_handle


class DatabaseWithMongodbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangoProject.database_with_mongodb"
    db_handle, client = get_db_handle(
        "cache_db", "cluster0.m0ojcry.mongodb.net", "27017", None, None
    )
