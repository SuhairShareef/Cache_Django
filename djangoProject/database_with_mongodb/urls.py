from .views import create_document, get_document, update_document, delete_document
from django.urls import path


urlpatterns = [
    # URL pattern for creating a document
    path("create/", create_document, name="create_document"),
    # URL pattern for getting a document by ID
    path("<str:document_id>/", get_document, name="get_document"),
    # URL pattern for updating a document by ID
    path("<str:document_id>/update/", update_document, name="update_document"),
    # URL pattern for deleting a document by ID
    path("<str:document_id>/delete/", delete_document, name="delete_document"),
]
