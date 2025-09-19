from django import forms
# from .models import Route

# class RouteForm(forms.ModelForm):
#     class Meta:
#         model = Route
#         fields = ["source", "destination", "duration"]

from .models import AirportNode
class AirportNodeForm(forms.ModelForm):
    class Meta:
        model = AirportNode
        fields = ["code", "position", "left", "right", "duration"]