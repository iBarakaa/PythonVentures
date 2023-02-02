import re

# search for the upper case character in word beginning and print the word
text = "I am the Last Dragon God Superman Sir"

# the initial instance of this code produces an error
for i in text.split():
    x = re.match(r"\bS\w+", i)
    print(x.group())