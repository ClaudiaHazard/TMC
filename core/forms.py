from django import forms
import datetime

class TMCForm(forms.Form):
    monto = forms.FloatField(label ='Monto', required=True)
    plazo = forms.IntegerField(label = 'Plazo', required=True)
    fecha = forms.DateField(label = 'Fecha', required=True, initial=datetime.datetime.now()-datetime.timedelta(days=15))
