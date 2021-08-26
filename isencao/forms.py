from django import forms
from .models import Perda

EVENTO_CHOICES = (('', u'-----'),) + Perda.EVENTO_CHOICES
TIPO_LAVOURA_CHOICES = (('', u'-----'),) + Perda.TIPO_LAVOURA_CHOICES

class PerdaForm(forms.ModelForm):
    class Meta:
        model = Perda
        fields = '__all__'

