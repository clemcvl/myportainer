# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import docker

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm, Docker


def index(request):

    return HttpResponse("Hello, world. You're at the polls indexssssss.")
# Create your views here.

def docker_updater(containers):

    for container in containers.keys():
        print('toto') 

def toto(request):

#    if request.method == 'POST':
#        print('toto') 
#        
#    client = docker.from_env()
#    containers = client.containers.list(all=True)
#    containers_active = client.containers.list(all=False)
#    a = ['toutou', 'tata']
#    completed = request.POST.get('lidarr', '') 
#    print(completed)
#    return render(request, "toto.html", {'toto_var': 'toto', 'titi_var': 'titi', 'a': a,
#                                         'containers': containers,
#                                         'containers_active': containers_active})
    client = docker.from_env()
    containers = client.containers.list()
    containers_active = client.containers.list(all=False)
    print('LAAAA')
    print(request.method)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print('In post')
        form = Docker(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data)
            for key, value in form.cleaned_data.iteritems():
            #for container in containers:
                print(key, value)
            # process the data in form.cleaned_data as required
            #name = form.cleaned_data['your_name']
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/toto')
    else:
        form = Docker()
        print(form)

    return render(request, 'toto.html', {'form': form,
                                        'containers': containers,
                                        'containers_active': containers_active})

def switch(request):

    client = docker.from_env()
    containers = client.containers.list()
    a = ['toutou', 'tata']
    return render(request, "switch.html", {'toto_var': 'toto', 'titi_var': 'titi', 'a': a,
                                         'containers': containers})
    # return render(request, "polls/toto.html", { 'toto_var' : 'titi' } )

def nametest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('toto')
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['your_name']
            print(name)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/toto')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('toto')
        form = NameForm()

    return render(request, 'name.html', {'form': form})
