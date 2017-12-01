import language_check


text = "i understand your project very well and i will complete this work within 24 hours . i have completed many similar projects before , so i hope you choose me to work with you."

import language_check
tool = language_check.LanguageTool('en-US')
matches = tool.check(text)
print(language_check.correct(text, matches))
