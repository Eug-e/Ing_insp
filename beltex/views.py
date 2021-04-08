from django.http import HttpResponse
from beltex.models import Specialists, Message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage



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

    if "fund" in request.POST:
        fund = 1.3
    else:
        fund = 1

    if "column" in request.POST:
        column = 1.1
    else:
        column = 1

    if "wall" in request.POST:
        wall = 1.5
    else:
        wall = 1

    if "over" in request.POST:
        over = 1.3
    else:
        over = 1

    if "roof" in request.POST:
        roof = 1.3
    else:
        roof = 1

    if "deta" in request.POST:
        deta = 1.3
    else:
        deta = 1

    z = round(int(volume) * 3 * fund * column * wall * over * roof * deta, 1)
    price = {'header': z}
    return render(request, 'Costs.html', context=price)

def inbox(request):
    name = request.POST['name']
    e_mail = request.POST['e_mail']
    phone_number = request.POST['phone_number']
    message = request.POST['message']
    client = Message(name=name, e_mail=e_mail, phone_number=phone_number, message=message)
    client.save()
    return render(request, 'home.html')

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

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'index.html')


