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

# View to create a new project
def new(request):

    if request.method == 'POST':
        # Get form fields
        project_name = request.POST.get('project-name')
        project_skills = request.POST.get('project-skills')
        project_learn = request.POST.get('project-learn')
        questions = request.POST.get('questions')
        min_bid = request.POST.get('min-bid')
        max_bid = request.POST.get('max-bid')

        print(project_skills)

        # Process POST data...
        # 1. Create project object
        budget = Budget(min_bid, max_bid)
        project = Project(project_name, project_learn, budget, [3,17])

        # 2. Call Freelancer API to post project, and retrieve project_id.
        store = ProjectStore()
        project_id = store.post_project(project)

        # 3. Store project_id in our local db.
        db_project = DBProject(project_id)
        db_project_store = DBProjectStore()
        db_project_store.add_project(db_project)

        # Redirect to success page
        return HttpResponseRedirect(reverse('hybridapp:success'))

        # N.B No error handling!!
        #15339120
        #15339110
        #15339118
    get_fl_project(15339120)

    return render(request, 'hybridapp/new.html')

# Page displayed upon successfully creating project.
def success(request):
    return render(request, 'hybridapp/success.html')
