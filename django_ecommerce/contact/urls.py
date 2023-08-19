from contact import views as contact_views
from django.urls import path

urlpatterns = [
    path("/contact", contact_views.contact, name="contact"),
]