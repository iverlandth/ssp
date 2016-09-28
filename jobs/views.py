from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

# Import api for users
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
# Create your views here.

from jobs.models import JobType, Job, ProfileJob, JobHistory
from jobs.form import JobTypeForm, JobForm, ProfileJobForm, JobHistoryForm


def jobtypes_index(request):
    jobtypes_all = JobType.objects.all()
    return render(request, 'jobtypes/index.html', {
        'jobtype_instance': JobType,
        'jobtypes': jobtypes_all,
    })


def jobtypes_new(request):
    if request.method == 'POST':
        form = JobTypeForm(request.POST)
        if form.is_valid():
            jobtype = form.save(commit=False)
            jobtype.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(jobtypes_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        form = JobTypeForm()
    return render(request, 'jobtypes/new.html', {
        'form': form,
    })


def jobtypes_edit(request, id):
    jobtype = JobType.objects.get(id=id)
    if request.method == 'POST':
        jobtype_form = JobTypeForm(request.POST, request.FILES, instance=jobtype)
        if jobtype_form.is_valid():
            save_jobtype = jobtype_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(jobtypes_index))
    else:
        jobtype_form = JobTypeForm(instance=jobtype)
    return render(request, 'jobtypes/edit.html', {
        'form': jobtype_form
    })


def jobtypes_show(request, id):
    jobtype = JobType.objects.get(id=id)

    return render(request, 'jobtypes/show.html', {
        'jobtype': jobtype,
        'jobtype_instance': JobType,
        'user_instance': User,
    })


def jobtypes_delete(request, id):
    jobtype = JobType.objects.get(id=id)
    jobtype.delete()
    is_exist = JobType.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(jobtypes_index))


# JOB HISTORIES
def jobhistories_index(request):
    jobhistories_all = JobHistory.objects.all()
    return render(request, 'jobhistories/index.html', {
        'jobhistory_instance': JobHistory,
        'jobhistories': jobhistories_all,
    })


def jobhistories_new(request, pj_id):
    if request.method == 'POST':
        form = JobHistoryForm(request.POST)
        if form.is_valid():
            jobhistory = form.save(commit=False)
            jobhistory.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(jobhistories_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        pj= ProfileJob.objects.get(pk=int(pj_id))
        form = JobHistoryForm(initial={'profilejob': pj})
    return render(request, 'jobhistories/new.html', {
        'form': form,
    })


def jobhistories_edit(request, id):
    jobhistory = JobHistory.objects.get(id=id)
    if request.method == 'POST':
        jobhistory_form = JobHistoryForm(request.POST, request.FILES, instance=jobhistory)
        if jobhistory_form.is_valid():
            save_jobhistory = jobhistory_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(jobhistories_index))
    else:
        jobhistory_form = JobHistoryForm(instance=jobhistory)
    return render(request, 'jobhistories/edit.html', {
        'form': jobhistory_form
    })


def jobhistories_show(request, id):
    jobhistory = JobHistory.objects.get(id=id)

    return render(request, 'jobhistories/show.html', {
        'jobhistory': jobhistory,
        'jobhistory_instance': JobHistory,
        'user_instance': User,
    })


def jobhistories_delete(request, id):
    jobhistory = JobHistory.objects.get(id=id)
    jobhistory.delete()
    is_exist = JobHistory.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(jobhistories_index))


# JOBS
def jobs_index(request):
    jobs_all = Job.objects.all()
    return render(request, 'jobs/index.html', {
        'job_instance': Job,
        'jobs': jobs_all,
    })


def jobs_new(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(jobs_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        form = JobForm()
    return render(request, 'jobs/new.html', {
        'form': form,
    })


def jobs_edit(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'POST':
        job_form = JobForm(request.POST, request.FILES, instance=job)
        if job_form.is_valid():
            save_job = job_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(jobs_index))
    else:
        job_form = JobForm(instance=job)
    return render(request, 'jobs/edit.html', {
        'form': job_form
    })


def jobs_show(request, id):
    job = Job.objects.get(id=id)

    return render(request, 'jobs/show.html', {
        'job': job,
        'job_instance': Job,
    })


def jobs_delete(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    is_exist = Job.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(jobs_index))


# PROFILE JOBS
def profilejobs_index(request):
    profilejobs_all = ProfileJob.objects.all()
    return render(request, 'profilejobs/index.html', {
        'profilejob_instance': ProfileJob,
        'profilejobs': profilejobs_all,
    })


def profilejobs_new(request, j_id):
    if request.method == 'POST':
        form = ProfileJobForm(request.POST)
        if form.is_valid():
            profilejob = form.save(commit=False)
            profilejob.save()
            message = 'Registrado correctamente!'
            messages.add_message(request, messages.SUCCESS, message)
            return HttpResponseRedirect(reverse(profilejobs_index))
        else:
            message = 'Existen errores por favor verifica!.'
            messages.add_message(request, messages.ERROR, message)
    else:
        job = Job.objects.get(pk=int(j_id))
        form = ProfileJobForm(initial={'job': job})
    return render(request, 'profilejobs/new.html', {
        'form': form,
    })


def profilejobs_edit(request, id):
    profilejob = ProfileJob.objects.get(id=id)
    if request.method == 'POST':
        profilejob_form = ProfileJobForm(request.POST, request.FILES, instance=profilejob)
        if profilejob_form.is_valid():
            save_profilejob = profilejob_form.save()

            message = "actualizado Correctamente"
            messages.add_message(request, messages.INFO, message)
            return HttpResponseRedirect(reverse(profilejobs_index))
    else:
        profilejob_form = ProfileJobForm(instance=profilejob)
    return render(request, 'profilejobs/edit.html', {
        'form': profilejob_form
    })


def profilejobs_show(request, id):
    profilejob = ProfileJob.objects.get(id=id)

    return render(request, 'profilejobs/show.html', {
        'profilejob': profilejob,
        'profilejob_instance': ProfileJob,
    })


def profilejobs_delete(request, id):
    profilejob = ProfileJob.objects.get(id=id)
    profilejob.delete()
    is_exist = ProfileJob.objects.filter(id=id).exists()

    if is_exist:
        message = 'No se pudo eliminar'
        messages.add_message(request, messages.ERROR, message)
    else:
        message = 'Eliminado!'
        messages.add_message(request, messages.SUCCESS, message)

    return HttpResponseRedirect(reverse(profilejobs_index))
