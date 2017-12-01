import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from hybridapp.models import Budget, Project, ProjectStore, DBProject, DBProjectStore

# Import API calls
from hybridapp.services import *

# Import models
from hybridapp.models import *

# Homepage
def home(request):
    return render(request, 'hybridapp/home.html')

# Dashboard
def dashboard(request):
    return render(request, 'hybridapp/dashboard.html')

# Projects
def projects(request):
    return render(request, 'hybridapp/projects.html')

# Logout
def logout(request):
    return HttpResponseRedirect(reverse('hybridapp:home'))

# View to create a new project
def new(request):
    print(request.method)
    if request.method == 'POST':
        # Get form fields
        project_name = request.POST.get('project-name')
        project_skills = request.POST.get('project-skills')
        project_learn = request.POST.get('project-learn')
        questions = request.POST.get('questions')
        min_bid = request.POST.get('min-bid')
        max_bid = request.POST.get('max-bid')

        # Process POST data here once the html template and form
        # is finished.

        # Create new project in our db
        # new_project()

        # Create new project using freelancer API
        # new_fl_project()

        # Redirect to home page
        return HttpResponseRedirect(reverse('hybridapp:success'))

    # Testing
    budget = Budget(100, 200)
    project = Project("Matt Test", "Description test", budget, [3,17])
    store = ProjectStore()
    project_id = store.post_project(project)

    db_project = DBProject(project_id)
    db_project_store = DBProjectStore()
    db_project_store.add_project(db_project)

    # End Testing
    return render(request, 'hybridapp/new.html')

# Page displayed upon successfully creating project.
def success(request):
    return render(request, 'hybridapp/success.html')
