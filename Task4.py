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

text_numbers = []   # stores all numbers which are making messages 
text_numbers_rec =[]  # stores all the received messages in text csv
calls_rec = []  # stores all the received calls in calls csv
calls_telemart = [] # These are the sure telemarts number
final_set = set()
# Storing all the text numbers inside a separate list to match with later on
for number in texts:
    text_numbers.append(number[0])
    text_numbers_rec.append(number[1])

    


for rec_number in calls:
    calls_rec.append(rec_number[1])
    
for item in calls:
    
    if item[0][:3] == "140":        
        calls_telemart.append(item[0])
    if item[0] not in text_numbers and item[0] not in text_numbers_rec and item[0] not in calls_rec:
        final_set.add(item[0])

calls_telemart_set = set(calls_telemart)
final_telemart = calls_telemart_set.union(final_set)

'''
for item in texts:
    if item[0][:3] == "140":
        if item[0] not in calls_telemart:
            final_telemart.add(item[0])
'''

#print(len(calls_telemart))
#print(len(final_set))
#print(len(final_telemart))
#print(len(final_telemart))
sortedlist = sorted(final_telemart)

print("These numbers could be telemarketers: ")

print('\n'.join(sortedlist))



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
'''
r = set([3,4,5,2,2])

a = [100, 1, 0, 22, 33, 5, 55]
a_str = []
for item in a:
    a_str.append(str(item))
a_str.sort()
a_str = " ".join(map(str,a))
str(a).sort()
for item in a:
    if item:
4015/10
a.sort()


def lenDigits(x):
    """
    Assumes int(x)
    """

    x = abs(x)

    if x < 10:
        return 1

    return 1 + lenDigits(x / 10)
lenDigits(4098)
'''

