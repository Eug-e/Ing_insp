
from django.http import HttpResponse
from beltex.models import Specialists, Men
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
import csv

from django.utils.translation import ugettext as _

# def translate(request):
#     return render_to_response(
#         'index.html',
#         {'title': _('Контакты')}
#     )

def index(request):
    return HttpResponse("привет")

def str1(request):
    x = Men.objects.filter(name='Hog')
    y = x[0]
    return HttpResponse(y.name)

def Ver(request):
    z = Specialists.objects.filter(specialist="Tacko Fall")
    w = z[0]
    return HttpResponse(w.car)

def ex41(request):

    return render(request,
        'index.html',
    {'start': 0, 'finish': 40}
    )

def login_user (request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'invalid.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('line4')

def log_out (request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('line4')
    else:
        return render(request,
                      'index.html',
                      {}
                      )

def First (request):
    return render(request, 'First.html')

def Second (request):
    return render(request, 'Second.html')

def Common (request):
    return render(request, 'Common.html')

def Reg (request):
    user = User.objects.create_user(
        request.POST['login'],
        password1=request.POST['password1'],
        password2=request.POST['password2'],
        first_name=request.POST['reg_name'],
        last_name=request.POST['reg_surname'],
        email=request.POST['reg_email']
    )
    return HttpResponse('ok')

def Form (request):
    return render(request, 'Registration.html')

def Ajax_path (request):
    response = {
        'message': request.POST['a'] + 'world'
    }
    return JsonResponse(response)

def Aja (request):
    response = {
        'mess': request.POST['a']
    }
    return JsonResponse(response)

def back (request):
    return HttpResponseRedirect('line4')

def Costs (request):
    return render(request, 'Costs.html')

def Spec (request):
    return render(request, 'spec.html')

def Obj (request):
    return render(request, 'objects.html')

def contacts (request):
    return render(request, 'Contacts.html')

def server (request):
    Men.objects.filter(
        id=request.POST['id']
    ).update(
        name=request.POST['name'],
        age=int(request.POST['age'])
    )
    return JsonResponse({'status':'ok'})

def server2 (request):
    Men.objects.filter(
        id=request.GET['id']
    )

    return JsonResponse({'status':'ok'})

def cost(request):
    x = request.POST["volume"]
    if x == '10':
        return render(request, 'Costs.html', context='no')
    else:
        z = int(x) * 3
        y = {'header': z}
        return render(request, 'Costs.html', context=y)

def get_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name'])
    persons = Men.objects.filter(
        age__gt= int(request.GET['start']),
        age__lt=int(request.GET['finish']),
    )
    for person in persons:
        writer.writerow([person.name, person.name])
    return response