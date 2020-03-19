import re
hand = open("data.txt").read()
y = re.findall("[0-9]+",hand)
print(y)                               #it return the list of value of the numbers present in file 
p = 0
for i in y:
    p = int(i) + p
print(p)                               #it return sum of all numbers present in file.


