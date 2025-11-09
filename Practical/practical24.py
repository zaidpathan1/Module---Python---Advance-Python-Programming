import re

text = "Welcome to TechFix Solutions, your gadget repair center."

word = "TechFix"

if re.search(word, text):
    print(f"The word '{word}' was found in the text.")
else:
    print(f"The word '{word}' was NOT found in the text.")