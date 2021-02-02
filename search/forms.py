from django.forms import ModelForm,TextInput
from main.models import Films

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['name']