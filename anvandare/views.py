from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def registrera(request):
    if request.method == 'POST':
        formular = UserRegisterForm(request.POST)
        if formular.is_valid():
            formular.save()
            anvandarnamn = formular.cleaned_data.get('username')
            messages.success(request, f'Konto skapades för {anvandarnamn}')
            return redirect('loggain')
    else:
        formular = UserRegisterForm()
    return render(request, 'anvandare/registrera.html', {'formular':formular})

@login_required
def profil(request):
    if request.method=='POST':
        u_formular = UserUpdateForm(request.POST,instance=request.user)
        p_formular = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profil)

        if u_formular.is_valid() and  p_formular.is_valid():
            u_formular.save()
            p_formular.save()
            messages.success(request, f'Din profil har uppdateras')
            return redirect('profil')

    else:
        u_formular = UserUpdateForm(instance=request.user)
        p_formular = ProfileUpdateForm(instance=request.user.profil)

    formular = {'u_formular':u_formular, 'p_formular':p_formular}

    return render(request, 'anvandare/profil.html', formular)