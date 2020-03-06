from django import forms
import datetime

class TMCForm(forms.Form):
    monto = forms.FloatField(label ='Monto')
    plazo = forms.IntegerField(label = 'Plazo')
    fecha = forms.DateField(label = 'Fecha', initial=datetime.datetime.now())
