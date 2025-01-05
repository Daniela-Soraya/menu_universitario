# apps/comedor/forms.py
from django import forms
from datetime import date
from .models import Estudiante, Platillo, Menu, Calificacion, Comentario

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = '__all__'

class MenuForm(forms.ModelForm):
    platillos = forms.ModelMultipleChoiceField(
        queryset=Platillo.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Para usar checkboxes; puedes cambiar a SelectMultiple
        required=True
    )

    class Meta:
        model = Menu
        fields = ['fecha', 'platillos']  # Específicamente incluye estos campos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Si es un registro nuevo
            self.fields['fecha'].initial = date.today  # Establece la fecha de hoy como inicial
            
class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        