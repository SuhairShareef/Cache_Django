from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from djangoProject.cache.utils import app_cache
from .models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def student_list(request):
    """
    Retrieve a list of all students.
    """
    cache_key = "all_students"
    students = app_cache.cache_instance.get(cache_key)

    if students is None:
        students = list(Student.objects.all())
        app_cache.cache_instance.put(cache_key, students)

    if not students:
        response_data = {
            "status": "error",
            "message": "No students found",
            "data": [],
        }
        return JsonResponse(response_data)

    serializer = StudentSerializer(students, many=True)
    response_data = {
        "status": "success",
        "message": "Students retrieved successfully",
        "data": serializer.data,
    }
    return JsonResponse(response_data, safe=False)


@api_view(["GET"])
def view_student(request, std_number):
    """
    Retrieve details of a specific student.
    """
    cache_key = f"student_{std_number}"
    student = app_cache.cache_instance.get(cache_key)

    if student is None:
        student = get_object_or_404(Student, std_number=std_number)
        app_cache.cache_instance.put(cache_key, student)

    serializer = StudentSerializer(student)
    response_data = {
        "status": "success",
        "message": "Student retrieved successfully",
        "data": serializer.data,
    }
    return JsonResponse(response_data)


@api_view(["POST"])
def create_student(request):
    """
    Create a new student or retrieve an existing student with the same student number.
    """
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        std_number = serializer.validated_data["std_number"]
        student, created = Student.objects.get_or_create(
            std_number=std_number, defaults=serializer.validated_data
        )

        if created:
            response_data = {
                "status": "success",
                "message": "Student created successfully",
                "data": {"student_id": std_number},
            }
        else:
            response_data = {
                "status": "success",
                "message": "Student already exists",
                "data": {"student_id": std_number},
            }
        return JsonResponse(response_data)
    else:
        response_data = {
            "status": "error",
            "message": "Invalid data provided",
            "errors": serializer.errors,
        }
        return JsonResponse(response_data)


@api_view(["POST"])
def update_student(request, pk):
    """
    Update details of a specific student.
    """
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()
        response_data = {
            "status": "success",
            "message": "Student updated successfully",
        }
    else:
        response_data = {
            "status": "error",
            "message": "Invalid data provided",
            "errors": serializer.errors,
        }

    return JsonResponse(response_data)


@api_view(["DELETE"])
def delete_student(request, std_number):
    """
    Delete a student based on the provided student number (std_number).
    """
    student = Student.objects.filter(std_number=std_number).first()

    if student:
        student.delete()
        response_data = {
            "status": "success",
            "message": "Student deleted successfully",
        }
    else:
        response_data = {
            "status": "error",
            "message": "Student does not exist",
        }

    return JsonResponse(response_data)
