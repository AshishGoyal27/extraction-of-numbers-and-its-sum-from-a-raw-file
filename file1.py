import re
hand = open("data.txt").read()
y = re.findall("[0-9]+",hand)
p = 0
for i in y:
    p = int(i) + p
print(p)


