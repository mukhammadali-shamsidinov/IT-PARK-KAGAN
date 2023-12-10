from django import forms

from posts.models import Product, Lesson, Video


class AddCourseForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )


    class Meta:
        model = Product
        fields = '__all__'


class LessonAddForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'custom_username'}),
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class AddFullCompleteForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"