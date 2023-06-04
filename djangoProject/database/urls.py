from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="students-list"),
    path("<int:std_number>/", views.view_student, name="get_single_student"),
    path("create/", views.create_student, name="create-student"),
    path("edit/", views.update_student, name="edit-student"),
    path("delete/", views.delete_student, name="delete-student"),
]
