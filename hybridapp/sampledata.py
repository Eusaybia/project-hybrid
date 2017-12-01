import requests
import json

employer_access_token = "q77Wx5W1sRouMU0sgaHEWbwnVskT7s"
freelancer_access_token = "VYdGZfXkIRRfb1aTWyzL8ViT9b8idF"

def make_bid(project_id, bidder_id, amount, period, milestone_percentage, description):
    data = {
        "project_id": project_id,
        "bidder_id": bidder_id,
        "amount": amount,
        "period": period,
        "milestone_percentage": milestone_percentage,
        "description": description
    }
    headers = {
        'content-type': 'application/json',
        'freelancer-oauth-v1': freelancer_access_token,
    }

    params = (
        ('compact', ''),
    )

    data = json.dumps(data)

    r = requests.post('https://www.freelancer-sandbox.com/api/projects/0.1/bids/?compact',
            headers=headers, params=params, data=data)

    # Print response
    bid_response = r.json()
    if bid_response["status"] != "success":
        print(bid_response)
        return None
    return bid_response


def make_project(title, description, jobs):
    headers = {
        'content-type': 'application/json',
        'freelancer-oauth-v1': employer_access_token,
    }
    params = (
        ('compact', ''),
    )
    data = {
        "title": title,
        "description": description,
        "currency": {
            "code": "AUD",
            "id": 3,
            "sign": "$"
        },
        "budget": {
            "minimum": 50,
            "maximum": 150
        },
        "jobs": [{"id": job_id} for job_id in jobs]
    }

    data = json.dumps(data)

    r = requests.post('https://www.freelancer-sandbox.com/api/projects/0.1/projects/',
              headers=headers, params=params, data=data)

    project_json = r.json()
    if project_json["status"] != "success":
        # Print response
        print(r.json())
        return None
    return project_json["result"]


def get_fl_project(project_id):
    headers = {
        'content-type': 'application/json',
        # Using the API key for the 'testemployer' account
        'freelancer-oauth-v1': employer_access_token,
    }

    r = requests.get('https://www.freelancer-sandbox.com/api/projects/0.1/projects/15339120',
                     headers=headers)

    project_json = r.json()
    if project_json["status"] != "success":
        return None
    return project_json

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

    bids = r.json()['result']['bids']

    if len(bids) == 0:
        # List is empty
        bids = None

    return bids



employer_id = 25832201
freelancer_id = 25832153
user_input = input("New Project(p), new bid (b), or quit(q)? ")

while user_input != "q":
    if user_input == "p":
        projects = get_fl_projects_by_user_id(employer_id)
        if projects:
            print("Current projects")
            for project in projects:
                print(project["title"])
                print("Project id: " + str(project["id"]))
                print("")

        # Default project
        title = "Default project title"
        description = "Default project description"
        jobs = [3, 17]
        data = input("Enter project title (leave blank for default): ")
        if data:
            title = data
        data = input("Enter project description (at least 5 chars) (leave blank for default): ")
        if data:
            description = data
        data = input("Enter comma separated jobs (leave blank for default -- RECOMMENDED): ")
        if data:
            jobs = [int(x) for x in data.split(",")]

        # Make the project
        if make_project(title, description, jobs) == None:
            print("Making project was NOT successful")
        else:
            print("Project made successfully")

    elif user_input == "b":
        projects = get_fl_projects_by_user_id(employer_id)
        if projects:
            print("Current projects")
            for project in projects:
                print(project["title"])
                print("Project id: " + str(project["id"]))
                print("")
            project_id = int(input("Choose a project, enter its id: "))
            if get_fl_project(project_id) != None:
                bids = get_bids_by_project_id(project_id)
                if bids != None:
                    print("Bids:")
                    for bid in bids:
                        print("Bid amount: " + str(bid["amount"]))
                    print("")
                else:
                    print("No current bids")

                # Set some defaults
                bidder_id = freelancer_id
                amount = 100
                period = 5
                milestone_percentage = 100
                description = "This is the default description."
                data = input("Enter bid amount (leave blank for default): ")
                if data:
                    amount = int(data)
                data = input("Enter period (leave blank for default): ")
                if data:
                    period = int(data)
                data = input("Enter milestone percentage (int) (leave blank for default): ")
                if data:
                    milestone_percentage = int(data)
                data = input("Enter description (must be at least 5 chars) (leave blank for default): ")
                if data:
                    description = data

                if make_bid(project_id, bidder_id, amount, period, milestone_percentage, description) == None:
                    print("Bid was NOT successful")
                else:
                    print("Bid was successful")

            else:
                print("Invalid project id")
        else:
            print("There are no current projects")
    user_input = input("New Project(p), new bid (b), or quit(q)? ")
