from django import forms
from .models import Componente


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['nombre', 'categoria', 'valor', 'cantidad', 'ubicacion', 'notas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10kΩ, 100µF'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Caja roja, Bandeja 3'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
