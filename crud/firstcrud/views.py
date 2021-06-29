from django.shortcuts import redirect, render
from .forms import AddUser, DeleteUser, UpdateForm
from .models import User
# Create your views here.

def index(request):
    form = AddUser(request.POST)
    if form.is_valid():
        user = User(name=form.cleaned_data['name'],
                    surname=form.cleaned_data['surname'])
        user.save()
    users = User.objects.all()

    return render(request, 'index.html', {'form': form, 'users':users})




def delete(request):
    form = DeleteUser(request.POST)
    users = User.objects.all()
    if form.is_valid():
        User.objects.get(id=form.cleaned_data['id']).delete()
        return redirect('index')
    return render(request, 'delete.html', {'form': form, 'users':users})


def update(request):
    form = UpdateForm(request.POST)
    users = User.objects.all()
    if form.is_valid():
        user = User.objects.get(id=form.cleaned_data['id'])
        user.name = form.cleaned_data['name']
        user.surname = form.cleaned_data['surname']
        user.save()
        return redirect('index')
    
    return render(request, 'update.html', {'form': form, 'users':users})