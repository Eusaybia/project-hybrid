from django.test import TestCase

from hybridapp.models import Bid, ProseLint, PyEnchant, Pedant, LanguageCheck

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
        text3 = "Good day in django developer since 3 years. At my portfolio i have several proects i did using Django. Feel free to contact me for any question or comment [9:48] I’m excited to share with you the proposal ,i am an expert in project you mentioned , Imagination and creativity can change the world . we are creative and imaginative We guarantee you to submit the work within timeline and as per your expectations. i understand your project very well and i will complete this work within 24 hours . i have completed many similar projects before , so i hope you choose me to work with you. I will help you untill you get fulfilled from my work. We’ll provide a level of service that is unbeaten and unmatched in quality and efficiency! Wind, rain, or shine, we’re here for you everyday 365 days of the year, 24 hours a day, 7 days a week. Who else can say that, You’re only a couple keyboard clicks away from being connected to a reliable Freelancer, I will fix your problem in the shortest amount of allotted time. We provide an unbeatable freelancing service experience and will work to solve every single one of your problem’s until you(our client), are completely satisfied."
        text4 = "Few words about my approach: I am into testing, SOLID, DRY, KISS - and I mean not just reading about it but bringing it into daily routine. I've introduced code style guidelines in two companies I've been working for so one could say I care a lot about stuff like PEP8 and linters. In fact I care a lot about code cleanliness and beauty in overall which is getting really nerdy. Sometimes I hope it doesn't look like bragging so here's the deal - I suggest I make a quick review of your app on the topic of your choice, something that will not take longer than, say, 15 minutes; let's call it a trial. In case you're satisfied with the results we can continue with what can hopefully become a long-term collaboration."
        
        text5 = "Few word about my approach: I am into testng, SOLID, DRY, KISS - and I mean not just reading about it but bringing it into day routine .I've introduced code style guidelines in two companies I've beenworking for so one could say I care a lot about stuff like PEP8 and linters. In fact I care lot about code cleanliness and beauty in overall which is getting really nerdy sometimes I hope it doesn't look like bragging so here's the deal - I suggest I make a quick review of your app on the topic of your choice, something that will not take longer than, say, 15 minutes; let's call it a trial. In case you're satisfied with the results we can continue with what can hopefully become a long-term collaboration."
        
        text6 = "Few word about my approach: I am into testng, SOLID, DRY, KISS - and i mean not just reading about it but bring it into day routine .I've introduced code style guidelines in to companies I've beenworking for so won could say I care a lot about stuff like PEP8 and linters. In fact I care lot about code clean and beaut in overall which is getting really nerdy sometimes I hope it doesn't look like bragging so here's the deal - I suggest I make a quick review of your app on the topic of your choice, something that will not take longer than say 15 minutes let's call it a try. In case you're satisfied with the results we can continue with what can hopefully become a long-term collaboration."
        
        text7 = "hi Conway, i will tell you a few things about my experience as a   programmer .I have worked as senoir softwareengineer in Dehli for the last 9 years . Their are many technologies i have used, such as Flask,, SQLAlchemy, and the Freelancer API ."
        
        text8 = "Good morning, i believe that i am the best prgrammer    for the job . Plese consider pickingme to do this project for you. "
        
        score = Bid.get_quality_score(text0)
        print("0")
        print(score)
        score = Bid.get_quality_score(text1)
        print("1")
        print(score)
        score = Bid.get_quality_score(text2)
        print("2")
        print(score)
        score = Bid.get_quality_score(text3)
        print("3")
        print(score)
        
        score = Bid.get_quality_score(text4)
        print("4")
        print(Bid.get_total_errors(text4))
        print(score)
        
        score = Bid.get_quality_score(text5)
        print("5")
        print(Bid.get_total_errors(text5))
        print(score)
        
        score = Bid.get_quality_score(text6)
        print("6")
        print(Bid.get_total_errors(text6))
        print(score)
        print(LanguageCheck.fix(text6))
        
        score = Bid.get_quality_score(text7)
        print("7")
        print(Bid.get_total_errors(text7))
        print(score)
        print(LanguageCheck.fix(text7))
        
        score = Bid.get_quality_score(text8)
        print("8")
        print(Bid.get_total_errors(text8))
        print(score)
        print(LanguageCheck.fix(text8))
        
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
