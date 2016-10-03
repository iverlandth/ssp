# encoding:utf-8
from django.utils import timezone

from users.models import Profile
from django.shortcuts import render
from users.form import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

# Import api for users
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response


def profiles_index(request):
    profiles_all = Profile.objects.all()
    return render(request, 'profiles/index.html', {
        'profiles': profiles_all,
    })


def profiles_new(request):
    if request.method == 'POST':
        formUser = UserCreationForm(request.POST)
        form = ProfileForm(request.POST)
        if formUser.is_valid() and form.is_valid():
            user = formUser.save()
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(profiles_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        formUser = UserCreationForm()
        form = ProfileForm()
    return render(request, 'profiles/new.html', {
        'form': form,
        'form_second': formUser,
    })


def profiles_edit(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            save_profile = profile_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(profiles_index))
    else:
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit.html', {
        'form': profile_form
    })


def profiles_show(request, id):
    profile = Profile.objects.get(id=id)

    return render(request, 'profiles/show.html', {
        'profile': profile,
        'profile_instance': Profile,
        'user_instance': User,
    })

def profiles_user_show(request, u_id):
    if not Profile.objects.filter(user_id=u_id).exists():
        message = "No existe perfil para este usuario"
        messages.add_message(request, messages.INFO, message)
        return HttpResponseRedirect(reverse(profiles_index))
    profile = Profile.objects.get(user_id=u_id)

    return render(request, 'profiles/show.html', {
        'profile': profile,
        'profile_instance': Profile,
        'user_instance': User,
    })


def profiles_delete(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    is_exist = Profile.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(profiles_index))


def log_in(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/private')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    if access.is_superuser:
                        return HttpResponseRedirect('/admin/')
                    else:
                        return HttpResponseRedirect('/')
                else:
                    return render(request, 'login/not_active.html')
            else:
                return render(request, 'login/not_user.html')
    else:
        form = AuthenticationForm()

    return render(request, 'login/imput_system.html', {
        'form': form
    })


@login_required(login_url='/log_in')
def private(request):
    usuario = request.user
    profile = Profile.objects.get(user=usuario)
    return render_to_response('login/private.html', {'usuario': usuario, 'profile': profile},
                              context_instance=RequestContext(request))


@login_required(login_url='/log_in')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
