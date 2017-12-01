from django.test import TestCase

from hybridapp.models import Bid, ProseLint, PyEnchant, Pedant

# Create your tests here.
class BidTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_scoring(self):
        text0 = "Hi,\
                Greetings for the day,\n\
                We do unrstand your neds and would love to help you out on this one.\n\
                We have en devping/maintaining various web applications in Python Django. Mostly these applications are hosted on clouds (AWS/Linode) and have SASS, CoffeeScript, AngularJS/JQuery, Bootstrap as front end technologies along with Python backend.\n\
                Few Pyth/Django applicions that we have worked on in the past are listed below for your quick reference:\n\
                "
        text1 = "Hi,\
                Greetings for the day,\n\
                We do understand your needs and would love to help you out on this one.\n\
                We have been developing/maintaining various web applications in Python Django. Mostly these applications are hosted on clouds (AWS/Linode) and have SASS, CoffeeScript, AngularJS/JQuery, Bootstrap as front end technologies along with Python backend.\n\
                Few Python/Django applications that we have worked on in the past are listed below for your quick reference:\n\
                "
        text2 = "I’m excited to share with you the proposal ,i am an expert in project you mentioned ,\
                Imagination and creativity can change the world .\
                we are creative and imaginative \
                We guarantee you to submit the work  within timeline and as per your expectations.\
                i understand your project very well and i will complete this work within 24 hours . i have completed many similar projects before , so i hope you choose me to work with you.\
                I will help you untill you get fulfilled from my work."
        bid = Bid(text0)
        score = bid.get_quality_score()
        print("0")
        print(score)
        bid1 = Bid(text1)
        score = bid1.get_quality_score()
        print("1")
        print(score)
        bid2 = Bid(text2)
        score = bid2.get_quality_score()
        print("2")
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
