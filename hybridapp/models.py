from django.db import models
from hybridapp.services import employer_access_token, freelancer_access_token
import requests
import json

import proselint
from enchant.checker import SpellChecker

# Create your models here.
class Bid():
    def __init__(self, text):
        self.text = text

    def get_quality_score(self):
        score = 0
        return score

    def get_suggestions(self):
        text = "Hello You don't have much code, that to do some review. Only I want say, that not need place business-logic in models. Like this"
        bid = Bid(text)

class ProseLint():
    @staticmethod
    def get_suggestions(text):
        suggestions = proselint.tools.lint(text)
        return suggestions

    @staticmethod
    def get_error_count(text):
        suggestions = proselint.tools.lint(text)
        return(len(suggestions))

# You need to install some dependecies for PyEnchant to work
# https://stackoverflow.com/questions/21083059/enchant-c-library-not-found-while-installing-pyenchant-using-pip-on-osx
class PyEnchant():
    @staticmethod
    def get_errors(text):
        checker = SpellChecker("en_AU")
        checker.set_text(text)
        return checker

    @staticmethod
    def get_error_count(text):
        checker = SpellChecker("en_AU")
        checker.set_text(text)
        return len(list(checker))

# Another class for punctuation checking
# https://github.com/Decagon/Pedant
# You need to
# sudo apt-get install nodejs
class Pedant():
    @staticmethod
    def validate(text):
        """validatejs = execjs.compile(
            validate : function(lines) {
                var inQuote = false;
                var currQuoteLength = 0;
                var quoteStartIndex = 0;
                var MAX_QUOTE_LENGTH = 20;
                var MAX_PUNCTUATION_LENGTH = 3;
                var punctuation = [ ',', '.', '!', ';', ';', '"' ];
                var punctuationAmount = 0;
                var punctuationStartIndex = 0;
                var quotes = [ '"', "'" ];
                var contractionEndings =
                    [ 't', 's', 'm', 're', 's', 've', 'd', 'll', 'em' ];

                function printError(msg, type, line, col) {
                console.log(msg + ", " + type + ", line " + (line + 1) + ", col " +
                            (col + 1));
                }

                lines = lines.split("\n");
                for (var j = 0; j < lines.length; j++) {
                text = lines[j];
                for (var i = 0; i < text.length; i++) {
                    if ("(".indexOf(text[i]) > -1) {
                    if ("(".indexOf(text[i + 1]) > -1) {
                        printError("too many parenthesis", "PunctuationError", j, i);
                    }
                    }

                    if (punctuation.indexOf(text[i]) > -1) {
                    if (punctuationAmount == 0) {
                        punctuationStartIndex = i;
                    }
                    punctuationAmount++;

                    if ((text[i + 1] != ")") && (text[i + 1] != " ")) {
                        printError("no space after punctuation", "PunctuationError", j,
                                punctuationStartIndex);
                    }

                    } else {
                    punctuationStartIndex = 0;
                    punctuationAmount = 0;
                    }
                    if (punctuationAmount > MAX_PUNCTUATION_LENGTH) {
                    printError("too much punctuation", "PunctuationError", j,
                                punctuationStartIndex);

                    punctuationStartIndex = 0;
                    punctuationAmount = 0;
                    }

                    // on a space
                    if (" ".indexOf(text[i]) > -1) {
                    if (((text[i + 1] == " ") || (text[i + 1] == ")"))) {
                        printError("too much whitespace", "WhitespaceError", j, i);
                    }
                    }
                    // found a quote that didn't end after sentence
                    if ((text[i + 1] == undefined) && inQuote) {
                    inQuote = false;
                    printError("unclosed quote", "QuoteError", j, quoteStartIndex);
                    }

                    // okay, we found a quote
                    if (quotes.indexOf(text[i]) > -1) {
                    // proper contraction detection using xor
                    var a = ((contractionEndings.indexOf(text[i + 1]) == -1));
                    var b = text[i] == "'";
                    var xor = (a ? !b : b);
                    if ((!inQuote) && !xor) {
                        quoteStartIndex = i;
                        inQuote = true;
                    } else {
                        if ((i - quoteStartIndex) > MAX_QUOTE_LENGTH) {
                        printError("quote too long", "QuoteError", j, quoteStartIndex);
                        inQuote = false;
                        }
                    }
                    }
                }
                }
            }
        )"""


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
