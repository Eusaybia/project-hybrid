import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Import API calls
from hybridapp.services import *

# Homepage
def home(request):
    return render(request, 'hybridapp/home.html')

# View to create a new project
def new(request):
    if request.method == 'POST':
        # Process POST data here once the html template and form
        # is finished.
        # Create new project in our db
        new_project()
        # Create new project using freelancer API
        new_fl_project()
    new_fl_project()
    return render(request, 'hybridapp/new.html')
