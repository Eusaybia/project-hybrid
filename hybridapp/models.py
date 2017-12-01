from django.db import models

import proselint
from enchant.checker import SpellChecker

# Create your models here.
class Bid():
    def __init__(self, text):
        self.text = text

    def get_quality_score(self):
        score = 0
        return score
    
    
class ProseLint():
    @staticmethod
    def get_suggestions(text):
        suggestions = proselint.tools.lint(text)
        return suggestions
    
    @staticmethod
    def get_error_count(text):
        suggestions = proselint.tools.lint(text)
        return(len(suggestions))

    
class PyEnchant():
    # You need to install some dependecies for PyEnchant to work
    # https://stackoverflow.com/questions/21083059/enchant-c-library-not-found-while-installing-pyenchant-using-pip-on-osx
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
        
    



