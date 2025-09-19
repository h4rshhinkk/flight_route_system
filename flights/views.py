from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import AirportNode
from .forms import AirportNodeForm
from django.db.models import Q
from .utils import nth_node, longest_path, shortest_between

# Create your views here.


class AirportCreateView(CreateView):
    model = AirportNode
    form_class = AirportNodeForm
    template_name = "flights/add_airport.html"
    success_url = reverse_lazy("add_airport")


class NthNodeView(TemplateView):
    template_name = "flights/nth_node.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.request.GET.get("root")
        n = self.request.GET.get("n")
        direction = self.request.GET.get("direction")
        node = None
        if code and n and direction:
            root = get_object_or_404(AirportNode, code=code)
            node = nth_node(root, int(n), direction.lower())
        context["result"] = node
        return context

class LongestRouteView(TemplateView):
    template_name = "flights/longest.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roots = AirportNode.objects.filter(left_parent__isnull=True,
                                           right_parent__isnull=True)
        if roots.exists():
            length, node = longest_path(roots.first())
            context["duration"] = length
            context["node"] = node
        return context

class ShortestBetweenView(TemplateView):
    template_name = "flights/shortest.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        src = self.request.GET.get("src")
        dest = self.request.GET.get("dest")
        if src and dest:
            start = get_object_or_404(AirportNode, code=src)
            goal = get_object_or_404(AirportNode, code=dest)
            dur, path = shortest_between(start, goal)
            context["duration"] = dur
            context["path"] = path
        return context