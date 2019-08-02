from django.shortcuts import render,redirect
from datetime import datetime
import math
import random
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from django.http import HttpResponse



# Create your views here.
def home1(request):
    return render(request,'index.html')


def add(request):
    date = datetime.now()
    c = ""

    if request.method == 'POST':
        a = request.POST.get('first')
        b = request.POST.get('second')
        c = "Result = " + str((int(a)+int(b)))
    return render(request, 'add.html', {'date': date, 'result': c})



def fact(request):
    f = ""

    if request.method == 'POST':
        a = request.POST.get('no')
        i = int(a)
        f = 1
        while(i>0):
            f = f*i
            i = i-1

    return render(request, 'factorial.html', {'resultfact': f})

def sqroot(request):
    r = ""

    if request.method == 'POST':
        a = request.POST.get('no')
        i = int(a)
        r = math.sqrt(i)
        print(a)

    return render(request, 'squareroot.html', {'resultsqrt': r})



def sign(request):
    m = ""
    form = FirstForm(request.POST)
    otp_gen = random.randint(1000, 9999)
    request.session['otp'] = otp_gen

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            print(name)
            mail_subject = "OTP verification from Technovalley"
            message = "Hai... "+str(name)+" Your verification code is "+str(otp_gen)

            try:
                abc = signin.objects.get(name=name)
                print(abc.name)
                if abc is not None:
                    m = "username already used"

            except:
                form.save()
                email = EmailMessage(mail_subject, message, to=[email])
                email.send()
                return redirect(otp)
    return render(request, 'signin.html', {'form': form, 'm': m})





def tables(request):
    abc = signin.objects.all()
    return render(request, 'tables.html', {'abc': abc})




def delete(request, id):
   ob = signin.objects.get(id=id)
   ob.delete()
   return redirect(tables)


def edit(request, id):
    abc = signin.objects.get(id=id)
    form = FirstForm(request.POST or None, instance=abc)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(tables)
    return render(request, 'signin.html', {'form': form})

def login(request):
    msg = ""
    if(request.method == 'POST'):
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            a = signin.objects.get(name=name, password=password)
            if a is not None:
                return redirect(home1)
        except:
            msg= "Invalid Login....Try somthing valid or get register..."
    return render(request, 'login.html', {'msg':msg})

def logintb(request):
    abc = log.objects.all()
    return render(request, 'logintb.html', {'abc': abc})


def deletelog(request, id):
    ob = log.objects.get(id=id)
    ob.delete()
    return redirect(logintb)

def editlog(request, id):
    abc = log.objects.get(id=id)
    form = LoginForm(request.POST or None, instance=abc)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(tables)
    return render(request, 'login.html', {'form': form})

def otp(request):
    msg=""
    if request.method == 'POST':
        otp_entr = request.POST.get('otp')
        otp_gen = request.session['otp']
        if int(otp_entr) == otp_gen:
            return redirect(home1)
        else:
            msg="Invalid OTP...Try again...."
    return render(request, 'otp.html', {'msg': msg})



# Create your views here.

def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')


# Python program to view
# for displaying images

def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
	    Hotels = Hotel.objects.all()
    return render(request, 'display_hotel_images.html', {'hotel_images' : Hotels})