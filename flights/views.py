from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Airport,Route
from .forms import RouteForm
from django.db.models import Q

# Create your views here.

class RouteCreateView(CreateView):
    model = Route
    form_class = RouteForm
    template_name = "flights/add_route.html"
    success_url = reverse_lazy("add_route")

class NthNodeView(TemplateView):
    template_name = "flights/nth_node.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        airport_code = self.request.GET.get("airport")
        n = self.request.GET.get("n")
        direction = self.request.GET.get("direction")

        result = None
        if airport_code and n and direction:
            airport = get_object_or_404(Airport, code=airport_code)
            qs = Route.objects.filter(Q(source=airport) | Q(destination=airport)).order_by("id")
            #direction
            # left → oldest to newest
            # right → newest to oldest
            if direction == "right":
                qs = qs.order_by("-id")
            #n=which position in the filtered, ordered list you want
            n = int(n)
            result = qs[n - 1] if qs.count() >= n else None

            

        context["result"] = result
        return context

class LongestRouteView(TemplateView):
    template_name = "flights/longest.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["route"] = Route.objects.order_by("-duration").first()
        return context


class ShortestBetweenView(TemplateView):
    template_name = "flights/shortest.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        departure = self.request.GET.get("departure")
        arrival = self.request.GET.get("arrival")

        route = None
        if departure and arrival:
            # Match either BLR->COK OR BLR->CCJ
            route = (
                Route.objects
                .filter(
                    Q(source__code=departure, destination__code=arrival) |
                    Q(source__code=arrival, destination__code=departure)
                )
                .order_by("duration")
                .first()
            )
        context["route"] = route
        return context
