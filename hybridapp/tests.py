from django.test import TestCase

from hybridapp.models import Bid

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
        text = "THis is no grammar.Lol"
        bid = Bid(text)
        suggestions = bid.get_suggestions()
        print("These are the following suggestions:")
        if suggestions is None:
            print("No suggestions")
        else:
            print(suggestions)

