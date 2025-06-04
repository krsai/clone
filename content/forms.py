from django import forms
from .models import Material, Movement

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description']

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['material', 'movement_type', 'quantity']
