from django import forms
from .models import ViewerData

class ViewerDataForm(forms.ModelForm):
    class Meta:
        model = ViewerData
        fields = ['name', 'email', 'location', 'is_raining']
        widgets = {
            'is_raining': forms.CheckboxInput(),
        }