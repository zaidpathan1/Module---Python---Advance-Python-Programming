import re

text = "Welcome to TechFix Solutions, your gadget repair center."

word = "Welcome"

if re.match(word, text):
    print(f"The text starts with the word '{word}'.")
else:
    print(f"The text does NOT start with the word '{word}'.")