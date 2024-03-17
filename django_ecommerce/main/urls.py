from main import views as main_views
from . import json_views
from django.urls import path

urlpatterns = [
    path("status_reports/", json_views.StatusCollection.as_view(), name="status_collection"),
    path("status_reports/<int:pk>/", json_views.StatusMember.as_view(), name="status_member"),
]
