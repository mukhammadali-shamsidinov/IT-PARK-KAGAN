from django.shortcuts import render, redirect
from django.views import View

from .forms import AddCourseForm, LessonAddForm, AddFullCompleteForm
# Create your views here.
from .models import Product, Video, Services


def landing(request):
    products = Product.objects.all().order_by('title')
    services = Services.objects.all()
    return render(request,'index.html',{"products":products,"services":services})

class DetailView(View):
    def get(self,request,id):
        uid = str(id)
        product = Product.objects.get(id=uid)
        for x in product.video_set.all():
            print(x.video_url.url)
        return render(request,'detail.html',{"product":product,"videos":['messi']})

class AddCourseView(View):
    def get(self,request):
        add = AddCourseForm()
        return render(request,'add_course.html',{"form":add})

    def post(self,request):
        add = AddCourseForm(data=request.POST,files=request.FILES)

        if add.is_valid():
            add.save()
            return redirect("posts:lesson")
        else:
            return render(request, 'add_course.html', {"form": add})


class LessonAddView(View):
    def get(self,request):
        form = LessonAddForm()
        return render(request,'lesson.html',{"form":form})

    def post(self,request):
        form = LessonAddForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("posts:add_full")
        else:
            return render(request, 'lesson.html', {"form": form})


class AddFullCourseView(View):
    def get(self,request):
        form = AddFullCompleteForm()
        return render(request,'addfull.html',{"form":form})

    def post(self,request):
        form = AddFullCompleteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:main")
        else:
            return render(request, 'addfull.html', {"form": form})