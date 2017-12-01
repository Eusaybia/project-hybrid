import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from hybridapp.models import Budget, Project, ProjectStore, DBProject, DBProjectStore

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
