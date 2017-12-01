from django.db import models

import proselint
from enchant.checker import SpellChecker
import execjs
import os
import sys

# Create your models here.
class Bid():
    def __init__(self, text):
        self.text = text

    def get_quality_score(self):
        score = 0
        return score
    
# Checks grammar
class ProseLint():
    @staticmethod
    def get_suggestions(text):
        suggestions = proselint.tools.lint(text)
        return suggestions
    
    @staticmethod
    def get_error_count(text):
        suggestions = proselint.tools.lint(text)
        return(len(suggestions))
    
    @staticmethod
    def fix(text):
        pass
        
# Checks spelling
# You need to install some dependecies for PyEnchant to work
# https://stackoverflow.com/questions/21083059/enchant-c-library-not-found-while-installing-pyenchant-using-pip-on-osx
# Reference for PyEnchant: http://pythonhosted.org/pyenchant/tutorial.html
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
        
# Checks punctuation
# https://github.com/Decagon/Pedant 
# You need to:
# make init-js
# Uses this as reference: https://www.codementor.io/jstacoder/integrating-nodejs-python-how-to-write-cross-language-modules-pyexecjs-du107xfep
class Pedant():
    @staticmethod
    def get_error_count(lines):
        runtime = execjs.get('Node')
        context = runtime.compile('''
            module.paths.push('%s');
            var pedant = require('pedantjs');
            function validate(lines) {
                return pedant.validate(lines);
            }
        ''' % os.path.join(os.path.dirname(__file__),'node_modules'))

        result = context.call("validate", lines)
        return result

# Another possible checker
# https://github.com/GitbookIO/rousseau
