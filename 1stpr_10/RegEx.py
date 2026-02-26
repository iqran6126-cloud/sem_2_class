import re
pattern = re.compile(r"")
print(type(pattern))
word = input("enter ur string")
pattern = re.compile(r"\d+")
result = pattern.sub("_",word)
print(result)