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
from main import views as main_views

from main.urls import urlpatterns as main_urlpatterns
from djangular_pools.urls import urlpatterns as djangular_pools_urlpatterns

main_urlpatterns.extend(djangular_pools_urlpatterns)

urlpatterns = [
    path("", main_views.index, name="home"),
    path('admin/', admin.site.urls),
    path("pages/", include("django.contrib.flatpages.urls")),
    path("contact/", contact_views.contact, name="contact"),
    
    # user registration/authentication
    path("sign_in/", users_views.sign_in, name="sign_in"),
    path("sign_out/", users_views.sign_out, name="sign_out"),
    path("register/", users_views.register, name="register"),
    path("edit/", users_views.edit, name="edit"),
    
    # api
    path("api/v1/", include("main.urls")),
]