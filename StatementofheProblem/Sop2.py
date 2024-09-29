def summarize(text, base_case):
    if text == base_case:
        return "Base case matched."
    else:
        # If the text doesn't match the base case, the program skips it
        return "Base case not matched, ignoring..."

text1 = "This is an example sentence."
text2 = "This is another example sentence."
base_case = "This is an example sentence."

print(summarize(text1, base_case)) 
print(summarize(text2, base_case))  