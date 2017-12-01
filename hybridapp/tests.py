from django.test import TestCase

from hybridapp.models import Bid, ProseLint, PyEnchant

# Create your tests here.
class BidTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_scoring(self):
        text = "THis is no grammar.Lol"
        bid = Bid(text)
        score = bid.get_quality_score()
        print(score)
        
    def test_suggestions(self):
        text = "Hello\
                You don't have much code, that to do some review. \
                Only I want say, that not need place business-logic in models. Like this"
        bid = Bid(text)
        suggestions = ProseLint.get_suggestions(bid.text)
        if suggestions is None:
            print("No suggestions")
        else:
            for suggestion in suggestions:
                print(suggestion)

