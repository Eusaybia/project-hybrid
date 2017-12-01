import requests

from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Homepage
def home(request):
    return render(request, 'hybridapp/home.html')

# View to create a new project
def new(request):
    if request.method == 'POST':
        # Process POST data here once the html template and form
        # is finished.
        headers = {
            'content-type': 'application/json',
            # Using the API key for the 'testemployer' account
            'freelancer-oauth-v1': '<oauth_access_token>',
        }
    return render(request, 'hybridapp/new.html')
