"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
call_log ={}
calls_set = set()

for item in calls:
    calls_set.add(item[0])
    calls_set.add(item[1])
    
for i in calls_set:
    call_log.setdefault(i,0)

for item in calls:
    #print(item)
    call_log[item[0]]+=int(item[3])
    call_log[item[1]]+=int(item[3])
    #call_duration.append(int(item[3]))

def findMaxValue(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))], max(v)

#phone_max = max(call_log.values())    
#print(phone_max)
#print(call_log[phone_maxID])
    
#max_duration = max(call_duration)
#max_id = call_duration.index(max_duration)
a,b = findMaxValue(call_log)
print("%s spent the longest time, %d seconds, on the phone during September 2016." %(a,b))




#print(calls[0])
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

'''
import operator
l = [4,5,6,44,7,8,8,10]
index, value = max(enumerate(l), key=operator.itemgetter(1))
print(index,value)

max_val = max(l)

max_idx = l.index(max_val)

a = [2, 9, -10, 5, 18, 9] 
max(xrange(len(a)), key = lambda x: a[x])

d = {'b':1,'a':4,'c':6}
a = max(d)
print(a,d[a])
a = sorted(d.values())

'''




