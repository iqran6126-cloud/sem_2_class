import re

text = "bond,james bond."

result = re.search(r"james", text)
if result:
    print("Found:", result.group())
else:
    print("Not found")
    