from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) #3
print(counter['green']) #1
print(dict(counter)) #{'red':2, 'blue':3, 'green':1}