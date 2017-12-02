import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import urlquote

from hybridapp.models import Budget, Project, ProjectStore, DBProject, DBProjectStore

# Import API calls
from hybridapp.services import *

# Import models
from hybridapp.models import *

client_id = "6e7e96c2-7e16-4c14-a818-331cea7cb35e"
client_secret = "b5e5908b29b395050352429de08efee54d00bfe7f93adf9cbb275b2b0ef98b8c78d716809e19d2fb6a79c872ace15a1c7ef7fb6c3b9d4413dfa8bfd1d9e9d970"

# Homepage
def home(request):
    return render(request, 'hybridapp/home.html')

# Dashboard
def dashboard(request):
    return render(request, 'hybridapp/dashboard.html')

# Projects
def projects(request):
    user_id = 25832201
    projects = get_fl_projects_by_user_id(request.session['access_token'], user_id)
    context = {
        'projects': projects
    }
    return render(request, 'hybridapp/projects.html', context=context)

# View to view bids for a specific project
def projectbids(request, project_id):
    bids = get_bids_by_project_id(request.session['access_token'], project_id)
    context = {
        'bids': bids
    }
    return render(request, 'hybridapp/projectbids.html', context=context)

# Logout
def logout(request):
    return HttpResponseRedirect(reverse('hybridapp:home'))

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
        project_id = store.post_project(request.session['access_token'], project)

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
    get_fl_project(request.session['access_token'], 15339120)

    return render(request, 'hybridapp/new.html')

# Page displayed upon successfully creating project.
def success(request):
    return render(request, 'hybridapp/success.html')

employer_scopes = "basic"
advanced_scopes = "1 3"
prompt = "select_account consent"

def oauth(request):
    return HttpResponseRedirect('https://accounts.freelancer-sandbox.com/oauth/authorise?' +
        'response_type=code&client_id=' + client_id +
        '&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fhybridapp%2Foauth%2Fredirect' +
        '&advanced_scopes=' + urlquote(advanced_scopes) +
        '&scope=' + urlquote(employer_scopes) +
        '&prompt=' + urlquote(prompt))

def oauth_redirect(request):
    if request.GET.get('error', '') != '':
        raise Exception('Failed to authenticate!')

    payload = {
        'grant_type': 'authorization_code',
        'code': request.GET.get('code', ''),
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': 'http://127.0.0.1:8000/hybridapp/oauth/redirect',
    }

    response = requests.post('https://accounts.freelancer-sandbox.com/oauth/token', data=payload)
    result = response.json()
    request.session['access_token'] = result['access_token']
    return HttpResponseRedirect(reverse('hybridapp:dashboard'))
