from django.http import HttpResponse
from beltex.models import Specialists, Archive
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
import csv
from django.utils.translation import ugettext as _

def index(request):
    return HttpResponse("привет")

# def str1(request):
#     x = Men.objects.filter(name='Hog')
#     y = x[0]
#     return HttpResponse(y.name)

def Ver(request):
    z = Specialists.objects.filter(id=1)
    w = z[0]
    return HttpResponse([w.age, w.skills, w.car])

def ex41(request):

    return render(request,
        'index.html',
    {'start': 0, 'finish': 40}
    )

def login_user (request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password'],
    )
    if user is None:
        return render(request, 'invalid.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('line4')

def log_out (request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('home')
    else:
        return render(request,
                      'home.html',
                      {}
                      )

# user registration
def Reg (request):
    user = User.objects.create_user(
        request.POST['login'],
        last_name=request.POST['reg_surname'],
        email=request.POST['reg_email'],
        password=request.POST['password'],
    )
    return HttpResponseRedirect('line4')

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

def guest (request):
    return render(request, 'home.html')

# def server (request):
#     Men.objects.filter(
#         id=request.POST['id']
#     ).update(
#         name=request.POST['name'],
#         age=int(request.POST['age'])
#     )
#     return JsonResponse({'status':'ok'})



def cost(request):
    volume = request.POST["volume"]

    # found = request.POST["foundations"]
    # col = request.POST["columns"]
    # wall = request.POST["walls"]
    # overlap = request.POST["overlap"]
    # roof = request.POST["roof"]
    # detail = request.POST["detail"]


    z = int(volume) * 3
    price = {'header': z}
    return render(request, 'Costs.html', context=price)

def inbox(request):
    name = request.POST['name']
    e_mail = request.POST['e_mail']
    phone_number = request.POST['phone_number']
    message = request.POST['message']
    client = Archive(object=name, specialist=e_mail)
    client.save()
    return render(request, 'home.html')



# def get_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = \
#         'attachment; filename="somefilename.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['id', 'name'])
#     persons = Men.objects.filter(
#         age__gt= int(request.GET['start']),
#         age__lt=int(request.GET['finish']),
#     )
#     for person in persons:
#         writer.writerow([person.name, person.name])
#     return response

def spec_upd(request):
    one = Specialists.objects.filter(id=1)
    two = Specialists.objects.filter(id=2)
    three = Specialists.objects.filter(id=3)
    four = Specialists.objects.filter(id=4)
    first = {'one': one}
    second = {'two': two}
    third = {'three': three}
    fourth = {'four': four}
    return render(request, 'spec.html', context=first)