
from django.http import HttpResponse
from beltex.models import Specialists
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.translation import ugettext as _

def translate(request):
    return render_to_response(
        'index.html',
        {'title': _('Контакты')}
    )


def index(request):
    return HttpResponse("привет")

def str1(request):
    x = Specialists.objects.filter(skills = 99)
    y = x[0]
    return HttpResponse(y.car)

def Ver(request):
    z = Specialists.objects.filter(specialist = "Veronica")
    w = z[0]
    return HttpResponse(w.car)

def ex41(request):

    return render (request,
        'index.html',
    {}
    )

def login_user (request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is None:
        return render (request, 'invalid.html', {})
    else:
        login (request, user)
        return HttpResponseRedirect('line4')

def log_out (request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('line4')
    else:
        return HttpResponse ('Ты не залогинен')

def First (request):
    return render (request, 'First.html')

def Second (request):
    return render (request, 'Second.html')

def Common (request):
    return render (request, 'Common.html')

def Reg (request):
    user = User.objects.create_user (
        request.POST['login'],
        password=request.POST['password'],
        first_name='first_name',
        last_name='last_name',
        email='e7y@ggg.by'
    )
    return HttpResponse ('ok')

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
    return render (request, 'Costs.html')

def Spec (request):
    return render (request, 'spec.html')

def Obj (request):
    return render (request, 'objects.html')

def contacts (request):
    return render (request, 'Contacts.html')