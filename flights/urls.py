from django.urls import path
from .views import (
    AirportCreateView,
    NthNodeView,
    ShortestBetweenView,
    LongestRouteView
)

urlpatterns = [
    path("add/", AirportCreateView.as_view(), name="add_airport"),
    path("nth/",NthNodeView.as_view(), name="nth_node"),
    path("longest/", LongestRouteView.as_view(), name="longest_route"),
    path("shortest/", ShortestBetweenView.as_view(), name="shortest_between"),
]
