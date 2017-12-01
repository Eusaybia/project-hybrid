import requests
import json

employer_access_token = "E1xFOLBVdL9QvAfXhgDu0nQjgh4O22"
freelancer_access_token = "VYdGZfXkIRRfb1aTWyzL8ViT9b8idF"

def new_fl_project():
    headers = {
        'content-type': 'application/json',
        # Using the API key for the 'testemployer' account
        'freelancer-oauth-v1': employer_access_token,
    }

    params = (
        ('compact', ''),
    )

    data = {
        "title": "Fix my PHP website",
        "description": "I wrote a small website in PHP but it does not work. I someone to fix it.",
        "currency": {
            "code": "AUD",
            "id": 3,
            "sign": "$"
        },
        "budget": {
            "minimum": 500
        },
        "jobs": [
            {
                "id": 3
            },
            {
                "id": 17
            }
        ]
    }

    data = json.dumps(data)

    r = requests.post(
        'https://www.freelancer-sandbox.com/api/projects/0.1/projects/',
        headers=headers, params=params, data=data
    )

    print(r.json())

def get_fl_project(project_id):
    headers = {
        'content-type': 'application/json',
        # Using the API key for the 'testemployer' account
        'freelancer-oauth-v1': employer_access_token,
    }

    r = requests.get('https://www.freelancer-sandbox.com/api/projects/0.1/projects/15339120',
                     headers=headers)

    print(r.json())

def get_fl_projects_by_user_id(user_id):
    headers = {
        'content-type': 'application/json',
        # Using the API key for the 'testemployer' account
        'freelancer-oauth-v1': employer_access_token,
    }

    params = (
        ('compact', ''),
        ('owners[]', [user_id]),
    )

    r = requests.get('https://www.freelancer-sandbox.com/api/projects/0.1/projects/',
                     headers=headers, params=params)

    projects = r.json()['result']['projects']

    if len(projects) == 0:
        # List is empty
        projects = None

    return projects
