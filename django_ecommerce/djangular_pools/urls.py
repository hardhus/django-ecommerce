from django.urls import path
from djangular_pools import json_views

urlpatterns = [
    path("polls/", json_views.PollCollection.as_view(), name="polls_collection"),
    path("polls/<int:pk>", json_views.PollMember.as_view()),
    path("poll_items/", json_views.PollItemCollection.as_view(), name="poll_items_collection"),
    path("poll_items/<int:pk>", json_views.PollItemMember.as_view()),
]