from django.db import models
from hybridapp.services import employer_access_token, freelancer_access_token
import requests
import json

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

# https://github.com/Decagon/Pedant
# You need to:
# make init-js
# Uses this as reference: https://www.codementor.io/jstacoder/integrating-nodejs-python-how-to-write-cross-language-modules-pyexecjs-du107xfep
class Pedant():
    @staticmethod
    def validate(lines):
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
