"""demo URL Configuration""""""
from django.urls import include
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from users import views

urlpatterns = [
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='home', template_name='users/logout.html'), name='logout'),

    path('about/', views.about, name='about'),
    #path('about/', auth_views.LogoutView.as_view(template_name='users/about.html'), name='about'),
    #path('Kids/', auth_views.LogoutView.as_view(template_name='users/kids.html'), name='kids'),
    path('kids/', views.kids, name='kids'),
    #path('men/', auth_views.LogoutView.as_view(template_name='users/men.html'), name='men'),
    path('men/', views.men, name='men'),
    #path('women/', auth_views.LogoutView.as_view(template_name='users/women.html'), name='women'),
    path('women/', views.women, name='women'),
    path('post/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)