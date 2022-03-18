from django.shortcuts import render, redirect

from .models import Students, Groups

from .form import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


def index(request):
    students = Students.objects.all()
    groups = Groups.objects.all()
    return render(request, 'Students/index.html', {'students': students, 'groups': groups})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'Students/students-add.html', {'form': form})

def group_add(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('index')
    else:
        form = GroupForm()
    return render(request, 'Students/groups-add.html', {'form': form})

#Регистрация
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization')
    else:
        form = UserCreationForm()
    return render(request, 'Students/registration.html', {"form": form})


#Авторизация
def authorization(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(index)
    else:
        form = AuthenticationForm()
    return render(request, 'Students/authorization.html', {"form": form})







