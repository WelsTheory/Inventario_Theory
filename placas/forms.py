from django import forms
from .models import Placa, Video


class PlacaForm(forms.ModelForm):
    class Meta:
        model = Placa
        fields = ['nombre', 'tipo', 'descripcion', 'ubicacion_fisica', 'directorio_pc', 'repo_url', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ubicacion_fisica': forms.TextInput(attrs={'class': 'form-control'}),
            'directorio_pc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '/home/usuario/proyectos/...'}),
            'repo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'url', 'descripcion', 'finalizado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/...'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'finalizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
