from .models import Post
from .models import Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_type', 'image_file', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
