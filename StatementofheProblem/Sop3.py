import re

memo = {}

def process_word(word):
    if word in memo:
        return memo[word]
    else:
        processed_word = re.sub(r'[^\w]', '', word) 
        memo[word] = processed_word
        return processed_word

text = "MASSIVE massive Massive."
words = text.split()

for word in words:
    print(f"Processing '{word}':", process_word(word))

print("Memoization dictionary:", memo)
