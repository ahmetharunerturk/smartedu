from django.urls import path
from courses import views


urlpatterns = [
    path('', views.course_list, name="courses"),
    path('<slug:category_slug>/<int:course_id>', views.course_detail, name="course_detail"),
]


