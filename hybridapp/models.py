from django.db import models
from hybridapp.services import employer_access_token, freelancer_access_token
import requests
import json

# Create your models here.
class Project(object):
    def __init__(self, title, description, budget, jobs):
        self._title = title
        self._description = description
        self._budget = budget
        self._jobs = jobs
    
    
    
    # Title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value
    
    # Description
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        if len(value) < 5:
            data = json.dumps(data)
        self._description = value
    
    # Budget
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    
    
    # Jobs
    @property
    def jobs(self):
        return self._jobs

    @jobs.setter
    def jobs(self, value):
        self._jobs = value



class Budget(object):
    def __init__(self, minimum, maximum):
        self._max = maximum
        self._min = minimum
    
    # Maximum
    @property
    def maximum(self):
        return self._max
    
    @maximum.setter
    def maximum(self, value):
        if value < self.minimum:
            raise ValueError("maximum cannot be less than minimum")
        self._max = value
    
    # Minimum
    @property
    def minimum(self):
        return self._min
    
    @minimum.setter
    def minimum(self, value):
        if value > self.minimum:
            raise ValueError("minimum cannot be greater than maximum")
        self._min = value


class DBProject(models.Model):
    object_id = models.IntegerField(primary_key=True)

class DBProjectStore(object):
    def add_project(self, project):
        project.save()
    
    def get_project_ids(self):
        return [x.object_id for x in DBProject.objects.all()]

class ProjectStore(object):
    
    def post_project(self, project):
        headers = {
            'content-type': 'application/json',
            'freelancer-oauth-v1': employer_access_token,
        }
        
        params = (
            ('compact', ''),
        )
        
        data = {
            "title": project.title,
            "description": project.description,
            "currency": {
                "code": "AUD",
                "id": 3,
                "sign": "$"
            },
            "budget": {
                "minimum": project.budget.minimum,
                "maximum": project.budget.maximum
            },
            "jobs": [{"id": job_id} for job_id in project.jobs]
        }
        
        data = json.dumps(data)
        
        r = requests.post('https://www.freelancer-sandbox.com/api/projects/0.1/projects/',
                  headers=headers, params=params, data=data)
        
        project_id = r.json()["result"]["id"]
        
        # Print response
        print(r.json())
        
        return project_id
        
        

if __name__ == "__main__":
    budget = Budget(100, 200)
    project = Project("Matt Test", "Description test", budget, [3,17])
    store = ProjectStore()
    project_id = store.post_project(project)
    
    db_project = DBProject(project_id)
    db_project_store = DBProjectStore()
    db_project_store.add_project(db_project)
