import re

text = "Dr. Smith loves programming. He works at Google. It's awesome!"
sentences = re.split(r'\. |\? |\! ', text)
print(sentences)
