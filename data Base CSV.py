import csv
import array
import os

with open('E:\\file.csv') as f:
    r= csv.reader(f, delimiter = ',')
    dict1 = {row[0:3] for row in r}

with open('E:\\test.csv') as f:
    r=csv.reader(f, delimiter=',')
    dict2={row[0:3] for row in r}

print (str(dict1))
print (str(dict2))

keys = set(dict1.keys() + dict2.keys())
with open('E:\\test.csv', 'wb') as f:
    w=csv.writer(f, delimiter=',')
    w.writerows([[key, dict1.get(key, "''"), dict2.get(key, "''")] for key in keys])