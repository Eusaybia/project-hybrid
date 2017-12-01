from django.db import models

import proselint

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
        suggestions = proselint.tools.lint(text)
        return suggestions




