from main import views as main_views
from django.urls import path

urlpatterns = [
    path("", main_views.index, name="home")
]
