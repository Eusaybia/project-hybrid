import requests
import json
import datetime
from hybridapp.models import Bid, LanguageCheck
employer_access_token = "q77Wx5W1sRouMU0sgaHEWbwnVskT7s"
freelancer_access_token = "VYdGZfXkIRRfb1aTWyzL8ViT9b8idF"

'''def new_fl_project():
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

    print(r.json())'''

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
    for project in projects:
        project['submitdate'] = datetime.datetime.fromtimestamp(project['submitdate'])

    if len(projects) == 0:
        # List is empty
        projects = None

    return projects

def get_bids_by_project_id(project_id):
    headers = {
        'content-type': 'application/json',
        # Using the API key for the 'testemployer' account
        'freelancer-oauth-v1': employer_access_token,
    }

    params = (
        ('compact', ''),
        ('projects[]', [project_id]),
    )

    r = requests.get('https://www.freelancer-sandbox.com/api/projects/0.1/bids/',
                     headers=headers, params=params)

    # print(r.json())
    bids = r.json()['result']['bids']
    for bid in bids:
        bid['submitdate'] = datetime.datetime.fromtimestamp(bid['submitdate'])
        bid_text = bid["description"]
        bid["quality_score"] = Bid.get_quality_score(bid_text)
        bid["fixed"] = LanguageCheck.fix(bid_text)
        errors = Bid.get_total_errors(bid_text)
        bid["num_errors"] = errors[0]
        bid["errors"] = "Errors found:<br>Language Check: " + str(errors[1]) + "<br>ProseLint: " \
            + str(errors[2]) + "<br>PyEnchant: " + str(errors[3]) + "<br>Pedant: " + str(errors[4])

    if len(bids) == 0:
        # List is empty
        bids = None

    return bids
