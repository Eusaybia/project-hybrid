import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Homepage
def home(request):
    return render(request, 'hybridapp/home.html')

# View to create a new project
def new(request):
    # Process POST data here once the html template and form
    # is finished.
    return render(request, 'hybridapp/new.html')
