from main import views as main_views
from . import json_views
from django.urls import include, path

urlpatterns = [
    path("status_reports/", json_views.StatusCollection.as_view(), name="status_reports_collection"),
    path("status_reports/<int:pk>/", json_views.StatusMember.as_view()),
    path("badges/", json_views.BadgeCollection.as_view(), name="badges_collection"),
    path("badges/<int:pk>/", json_views.BadgeMember.as_view()),
]
