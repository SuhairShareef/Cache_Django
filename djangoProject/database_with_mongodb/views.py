import json

from bson import ObjectId
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .apps import DatabaseWithMongodbConfig
from .utils import get_collection_handle
from .definitions import COLLECTION_NAME


@csrf_exempt
def create_document(request):
    db_handle = DatabaseWithMongodbConfig.db_handle
    print(db_handle)
    collection = get_collection_handle(db_handle, COLLECTION_NAME)
    data = request.POST.dict()  # Assuming form data is sent in the POST request
    inserted_id = collection.insert_one(data).inserted_id
    return JsonResponse({"message": f"Document created with ID: {inserted_id}"})


@csrf_exempt
def get_document(request, document_id):
    db_handle = DatabaseWithMongodbConfig.db_handle
    collection = get_collection_handle(db_handle, COLLECTION_NAME)
    document = collection.find_one({"_id": ObjectId(str(document_id))})

    if document:
        # Convert ObjectId to string
        document["_id"] = str(document["_id"])
        # Serialize document to JSON
        return JsonResponse(dict(document))
    else:
        return JsonResponse({"error": "Document not found"}, status=404)


@csrf_exempt
def update_document(request, document_id):
    db_handle = DatabaseWithMongodbConfig.db_handle
    collection = get_collection_handle(db_handle, COLLECTION_NAME)
    data = json.loads(request.body)  # Parse JSON data from request body
    result = collection.update_one({"_id": ObjectId(str(document_id))}, {"$set": data})
    if result.modified_count > 0:
        return JsonResponse({"message": "Document updated successfully"})
    else:
        return JsonResponse({"error": "Document not found"}, status=404)


@csrf_exempt
def delete_document(request, document_id):
    db_handle = DatabaseWithMongodbConfig.db_handle
    collection = get_collection_handle(db_handle, COLLECTION_NAME)
    result = collection.delete_one({"_id": ObjectId(str(document_id))})
    if result.deleted_count > 0:
        return JsonResponse({"message": "Document deleted successfully"})
    else:
        return JsonResponse({"error": "Document not found"}, status=404)
