import language_check

text = "Few words about my approach: I am into testing, SOLID, DRY, KISS - and I mean not just reading about it but bringing it into daily routine. I've introduced code style guidelines in two companies I've been working for so one could say I care a lot about stuff like PEP8 and linters. In fact I care a lot about code cleanliness and beauty in overall which is getting really nerdy sometimes I hope it doesn't look like bragging so here's the deal - I suggest I make a quick review of your app on the topic of your choice, something that will not take longer than, say, 15 minutes; let's call it a trial. In case you're satisfied with the results we can continue with what can hopefully become a long-term collaboration."

tool = language_check.LanguageTool('en-US')
matches = tool.check(text)
print(language_check.correct(text, matches))
