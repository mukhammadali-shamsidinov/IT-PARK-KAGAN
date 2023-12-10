from django.urls import path
from .views import RegisterView,LoginView,ProfileView,LogoutView,ProfileEditView,UserAllView,DeleteUserView,EditAllUserView

app_name="users"
urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('profile/',ProfileView.as_view(),name="profile"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('profile/edit/',ProfileEditView.as_view(),name="profile_edit"),
    path('all/',UserAllView.as_view(),name="all_user"),
    path('delete/<str:username>/',DeleteUserView.as_view(),name="delete_user"),
    path('edit/<str:username>/',EditAllUserView.as_view(),name="edit_user")

]