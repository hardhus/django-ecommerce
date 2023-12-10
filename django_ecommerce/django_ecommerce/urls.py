"""django_ecommerce URL Configuration

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
from users import views as users_views
from contact import views as contact_views

urlpatterns = [
    path("", include("main.urls")),
    path('admin/', admin.site.urls),
    path("pages/", include("django.contrib.flatpages.urls")),
    path("contact/", contact_views.contact, name="contact"),
    
    # user registration/authentication
    path("sign_in/", users_views.sign_in, name="sign_in"),
    path("sign_out/", users_views.sign_out, name="sign_out"),
    path("register/", users_views.register, name="register"),
    path("edit/", users_views.edit, name="edit"),
]