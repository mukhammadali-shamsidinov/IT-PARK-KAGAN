from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm, CustomAuthenticationForm, ProfileEditForm, EditProfileUsersForm
from users.models import CustomUser


# Create your views here.
class RegisterView(View):
    def get(self,request):
        user_form = RegisterForm()
        return render(request,'register.html',{"form":user_form})
    def post(self,request):
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("users:login")


class LoginView(View):
    def get(self,request):
        user_form = CustomAuthenticationForm()
        return render(request,'login.html',{"form":user_form})

    def post(self,request):
        user_form = CustomAuthenticationForm(data=request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request,user)
            return redirect("posts:main")
        else:
            return render(request, 'login.html', {"form": user_form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")


class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        context = {
            "user":user
        }

        return render(request,'profile.html',context)

class ProfileEditView(View):
    def get(self,request):
        user_form = ProfileEditForm(instance=request.user)
        context = {
            "form":user_form
        }

        return render(request,'profile-edit.html',context)

    def post(self,request):
        user_form = ProfileEditForm(instance=request.user,data=request.POST,files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect("users:profile")
        else:
            context = {
                "form": user_form
            }

            return render(request, 'profile-edit.html', context)


class UserAllView(View):
    def get(self,request):
        users = CustomUser.objects.all()
        return render(request,'users.html',{"users":users})

class DeleteUserView(View):
    def get(self,request,username):
        user = CustomUser.objects.get(username=username)
        user.delete()
        return redirect("users:all_user")


class EditAllUserView(View):
    def get(self,request,username):
        custom = CustomUser.objects.get(username=username)
        users = EditProfileUsersForm(instance=custom)
        return render(request,'edit_users.html',{"form":users})
    def post(self,request,username):
        custom = CustomUser.objects.get(username=username)
        users = EditProfileUsersForm(instance=custom,data=request.POST,files=request.FILES)

        if users.is_valid():
            users.save()
            return redirect("users:all_user")
        else:
            return render(request, 'edit_users.html', {"form": users})
