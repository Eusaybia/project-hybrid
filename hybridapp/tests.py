from django.test import TestCase

from hybridapp.models import Bid, ProseLint, PyEnchant, Pedant

# Create your tests here.
class BidTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_scoring(self):
        text = "THis is no grammar.Lol"
        bid = Bid(text)
        score = bid.get_quality_score()
        print(score)
        
class ProseLintTestCase(TestCase):
    def setUp(self):
        pass

    def test_suggestions(self):
        text = "Too many exclamation marks!!!!Also, missing space"
        suggestions = ProseLint.get_suggestions(text)
        if suggestions is None:
            print("No suggestions")
        else:
            for suggestion in suggestions:
                print(suggestion)
                
    def test_error_count(self):
        text = "Too many exclamation marks!!!! Too  many spaces too"
        error_count = ProseLint.get_error_count(text)
        actual_error_count = 2
        self.assertEquals(error_count, actual_error_count)
                
class PyEnchantTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_error_count(self):
        text = "Thiz txtt hazz three errors"
        error_count = PyEnchant.get_error_count(text)
        actual_error_count = 3
        self.assertEquals(error_count, actual_error_count)
        
class PedantTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_error_count(self):
        text = "The quick brown fox,jumped over,the lazy dog"
        error_count = Pedant.get_error_count(text)
        actual_error_count = 2
        self.assertEquals(error_count, actual_error_count)
