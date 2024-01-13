from django.forms import ModelForm
from .models import Journey

class JourneyForm(ModelForm):
    class Meta:
        model = Journey
        fields = ['from_location','to_location','date']