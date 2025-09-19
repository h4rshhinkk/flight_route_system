from django.urls import path
from .views import (
    RouteCreateView,
    NthNodeView,
    ShortestBetweenView,
    LongestRouteView

)

urlpatterns = [
    path("add/", RouteCreateView.as_view(), name="add_route"),
    path("nth/",NthNodeView.as_view(), name="nth_node"),
    path("longest/", LongestRouteView.as_view(), name="longest_route"),
    path("shortest/", ShortestBetweenView.as_view(), name="shortest_between"),
]
