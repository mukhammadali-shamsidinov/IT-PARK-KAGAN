from django.urls import path
from .views import landing,DetailView,AddCourseView,LessonAddView,AddFullCourseView

app_name="posts"
urlpatterns = [
    path('',landing,name="main"),
    path('detail/<uuid:id>/',DetailView.as_view(),name="detail"),
    path('add/',AddCourseView.as_view(),name="add_course"),
    path('lesson/',LessonAddView.as_view(),name="lesson"),
    path('complete/',AddFullCourseView.as_view(),name="add_full")
]