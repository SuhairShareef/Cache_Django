from django.urls import path
from . import views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("", views.student_list, name="students-list"),
    path("<int:std_number>/", views.view_student, name="get_single_student"),
    path("create/", views.create_student, name="create-student"),
    path("edit/<int:std_number>/", views.update_student, name="edit-student"),
    path("delete/<int:std_number>/", views.delete_student, name="delete-student"),
    path("users/", views.get_users),
]
