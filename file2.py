import re
print([i for i in re.findall("[0-9]+",open("data.txt").read())])
print(sum([int(i) for i in re.findall("[0-9]+",open("data.txt").read())]))
