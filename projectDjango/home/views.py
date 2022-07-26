from django.shortcuts import render, redirect
from datetime import datetime
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import sys
from subprocess import run, PIPE


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        myuser = User.objects.create_user(email, password)
        myuser.save()
        messages.success(request, 'Welcome!')
        return redirect('home')
    return render(request, 'login.html')


def external(request):
    image = request.FILES['image']
    print('image is ', image)
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    fileurl = fs.open(filename)
    templateurl = fs.url(filename)
    print('file raw url', filename)
    print('file full url', fileurl)
    print('template url', templateurl)
    image = run([sys.executable, 'home/script/image.py', str(fileurl), str(filename)], shell=False, stdout=PIPE)
    print(image.stdout)
    return render(request, 'index.html', {'raw_url': templateurl, 'edit_url': image.stdout})
