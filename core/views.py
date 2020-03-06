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
            response = requests.get('https://api.sbif.cl/api-sbifv3/recursos_api/tmc/'+both+'?apikey=9f253b4442c3edf7b2f54a3e7b7e6ab6a8163bdb&formato=json')
            data=response.json()
            values=data['TMCs']
            context['val']=data['TMCs']
            print(values)
            for i in values:
                print(i['Titulo'])
                if(i['Titulo']!=None):
                    if(plazo>=365 and ('De un año o más' in i['Titulo'] or 'De un año o más' in i['SubTitulo'])):
                        if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'] or 'Superiores al equivalente de 2000' in i['SubTitulo']) or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 200) and ('Superiores al equivalente de 200 ' in i['SubTitulo'] )):
                            context['val'] = i
                        elif ((monto < 50) and ('Inferiores' in i['SubTitulo'] and ('50' or '200' or '2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 200) and ('Inferiores' in i['SubTitulo'] and ('5.000' or '200' or '2.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 2000) and ('Inferiores' in i['SubTitulo'] and ('2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 5000) and ('Inferiores' in i['SubTitulo'] and ('5.000' in i['SubTitulo']))):
                            context['val'] = i
                    elif (plazo >= 90) and  (('90 días o más' in i['Titulo']) or ('Menores a un año' in i['Titulo'])):
                        if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'] or 'Superiores al equivalente de 2000' in i['SubTitulo']) or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 200) and ('Superiores al equivalente de 200 ' in i['SubTitulo'] )):
                            context['val'] = i
                        elif ((monto < 50) and ('Inferiores' in i['SubTitulo'] and ('50' or '200' or '2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 200) and ('Inferiores' in i['SubTitulo'] and ('5.000' or '200' or '2.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 2000) and ('Inferiores' in i['SubTitulo'] and ('2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 5000) and ('Inferiores' in i['SubTitulo'] and ('5.000' in i['SubTitulo']))):
                            context['val'] = i
                    elif(plazo < 90) and (('menores de 90 días' in i['Titulo']) or ('Menores a un año'in i['Titulo']) or 'menos de 90 ' in i['Titulo']):
                        if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'] or 'Superiores al equivalente de 2000' in i['SubTitulo']) or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 200) and ('Superiores al equivalente de 200 ' in i['SubTitulo'] )):
                            context['val'] = i
                        elif ((monto < 50) and ('Inferiores' in i['SubTitulo'] and ('50' or '200' or '2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 200) and ('Inferiores' in i['SubTitulo'] and ('5.000' or '200' or '2.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 2000) and ('Inferiores' in i['SubTitulo'] and ('2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 5000) and ('Inferiores' in i['SubTitulo'] and ('5.000' in i['SubTitulo']))):
                            context['val'] = i
                    elif((plazo < 90 and ((' días o más' not in i['Titulo']) and ('año o más' not in i['Titulo']))) or ('Operaciones reajustables en moneda nacional' in i['Titulo']and ('año o más' not in i['SubTitulo']))):
                        if ((monto > 5000) and ('Superiores al equivalente de 5.000' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 2000) and ('Superiores al equivalente de 2.000' in i['SubTitulo'] or 'Superiores al equivalente de 2000' in i['SubTitulo']) or ('Inferiores o iguales al equivalente de 2000 unidades de fomento' in i['SubTitulo'])):
                            context['val'] = i
                        elif ((monto > 200) and ('Superiores al equivalente de 200 ' in i['SubTitulo'] )):
                            context['val'] = i
                        elif ((monto < 50) and ('Inferiores' in i['SubTitulo'] and ('50' or '200' or '2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 200) and ('Inferiores' in i['SubTitulo'] and ('5.000' or '200' or '2.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 2000) and ('Inferiores' in i['SubTitulo'] and ('2.000' or '5.000' in i['SubTitulo']))):
                            context['val'] = i
                        elif ((monto < 5000) and ('Inferiores' in i['SubTitulo'] and ('5.000' in i['SubTitulo']))):
                            context['val'] = i
            if context['val']!=data['TMCs']:
                context['tmc']='El TMC corresponde a '+context['val']['Valor']+'%.'
                context['val']='Sujeto a '+context['val']['Titulo']+', '+context['val']['SubTitulo']+'.' 
            else:
                context['val']='No encontrado'
                context['tmc']=''

    else: 
        form = TMCForm() 
    context['form'] = form


    return render(request, 'core/base.html', context)

    