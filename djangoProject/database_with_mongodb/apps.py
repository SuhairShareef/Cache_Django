from django.apps import AppConfig
from .utils import get_db_handle
from config import DATABASE


class DatabaseWithMongodbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangoProject.database_with_mongodb"
    db_handle, client = get_db_handle(
        db_name=DATABASE["NAME"],
        url=DATABASE["URL"],
    )
