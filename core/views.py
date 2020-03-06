from django.shortcuts import render
import requests
from .forms import TMCForm

# Create your views here.

def base(request):
    url=''
    ano=''
    mes=''
    context = {} 
    if request.method == "POST": 
        form = TMCForm(request.POST)
        if form.is_valid(): 
            temp = form.cleaned_data.get("monto") 
            print(type(temp))
            ano = request.POST['fecha'][:4]
            mes = request.POST['fecha'][5:7]
            monto = int(request.POST['monto'])
            plazo = int(request.POST['plazo'])
            print("PLAZO ES: ",plazo)
            both=ano+'/'+mes
            response = requests.get('https://api.sbif.cl/api-sbifv3/recursos_api/tmc/posteriores/'+both+'?apikey=9f253b4442c3edf7b2f54a3e7b7e6ab6a8163bdb&formato=json')
            data=response.json()
            values=data['TMCs']
            context['val']=data['TMCs']
            for i in values:
                print(i['Titulo'])
                if (plazo >= 90) and  (('90 días o más' in i['Titulo']) or ('Menores a un año' in i['Titulo'])):
                    if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                        context['val'] = i['Valor']
                    elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'])):
                        context['val'] = i['Valor']
                    elif ((monto > 200) and ('Superiores al equivalente de 200' in i['SubTitulo'] or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['Subtitulo']))):
                        context['val'] = i['Valor']
                elif(plazo < 90) and (('menores de 90 días' in i['Titulo']) or ('Menores a un año'in i['Titulo'])):
                    if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                        context['val'] = i['Valor']
                    elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'])):
                        context['val'] = i['Valor']
                    elif ((monto > 200) and ('Superiores al equivalente de 200' in i['SubTitulo'] or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['Subtitulo']))):
                        context['val'] = i['Valor']
                else:
                    if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                        context['val'] = i['Valor']
                    elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'])):
                        context['val'] = i['Valor']
                    elif ((monto > 200) and ('Superiores al equivalente de 200' in i['SubTitulo'] or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['Subtitulo']))):
                        context['val'] = i['Valor']

    else: 
        form = TMCForm() 
    context['form'] = form


    return render(request, 'core/base.html', context)

    