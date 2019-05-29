"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

texts_set = set()
calls_set = set()
for item in texts:
    texts_set.add(item[0])
    texts_set.add(item[1])
for item in calls:
    calls_set.add(item[0])
    calls_set.add(item[1])
print("There are %s different telephone numbers in the records." %(len(texts_set.union(calls_set))))

    

'''
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

'''

'''
s = {'a','b','c','d'}
se = set()
l = ['c','d','l kdji d','k','y','c']
for item in l:
    se.add(item)
print(se)

w = {'c','d','re','wd','dsfd'}
r = se.union(w)
se.add(34)


se = {'a','b'}
'''




