from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from djangoProject.cache.utils import app_cache


def get_routes(request):
    routes = [
        {
            "Endpoint": "/get/key",
            "method": "GET",
            "body": None,
            "description": "Returns data accordingly from the cache, if not existed returns None",
        },
        {
            "Endpoint": "/add/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Add item to the cache if not existed",
        },
    ]
    return JsonResponse(routes, safe=False)


@csrf_exempt
def cache_get(request):
    """
    Retrieve a value from the cache using GET request
    """
    key = request.GET.get("key")  # Assuming the key is passed as a query parameter

    # Retrieve the value from the cache
    value = app_cache.cache_instance.get(key)

    if value is not None:
        return JsonResponse({"key": key, "value": value})
    else:
        return JsonResponse({"message": "Key not found in cache"})


@csrf_exempt
def cache_put(request):
    """
    Store a value in the cache using POST request
    """
    key = request.POST.get("key")  # Assuming the key is passed in the request body
    value = request.POST.get(
        "value"
    )  # Assuming the value is passed in the request body

    # Store the value in the cache
    app_cache.cache_instance.put(key, value)

    return JsonResponse({"message": "Value stored in cache"})
