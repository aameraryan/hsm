from django.shortcuts import render, reverse
from django.urls import resolve
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Patient, Setting, Floor


def home(request):
    return HttpResponseRedirect('/admin/')


def screen_request(request):
    return HttpResponseRedirect(reverse('portal:display_screen', kwargs={'floor_id': request.user.floor.id}))


def display_screen(request, floor_id):
    my_floor = Floor.objects.get(id=floor_id)
    patients = Patient.objects.filter(Floor=my_floor, Discharged=False).order_by('Room')
    context = {'patients': patients, 'hospital': Setting.objects.first(), 'floor': my_floor}
    return render(request, 'portal/display_screen.html', context)


def floor_list(request):
    if request.user.is_superuser:
        context = {'floor_list': Floor.objects.all().order_by('Name')}
        return render(request, 'portal/floor_list.html', context)
    else:
        return HttpResponse('This is only for Admin')
