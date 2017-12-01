import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Import API calls
from hybridapp.services import *

# Import models
from hybridapp.models import *

# Homepage
def home(request):
    return render(request, 'hybridapp/home.html')

# View to create a new project
def new(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST.get('project-name'))
        # Process POST data here once the html template and form
        # is finished.
        # Create new project in our db
        # new_project()
        # Create new project using freelancer API
        # new_fl_project()
        # Redirect to home page
        return HttpResponseRedirect(reverse('hybridapp:success'))
    return render(request, 'hybridapp/new.html')

# Page displayed upon successfully creating project.
def success(request):
    return render(request, 'hybridapp/success.html')
