from django.contrib import admin
from .models import Product,Video,Category,Lesson,Services,MyBlog
# Register your models here.
admin.site.register(Product)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Services)
admin.site.register(MyBlog)
