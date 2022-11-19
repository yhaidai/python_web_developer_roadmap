from django import forms

from .models import RoadmapItem


class RoadmapItemForm(forms.ModelForm):
    class Meta:
        model = RoadmapItem

        widgets = {
            "description": forms.Textarea,
        }
