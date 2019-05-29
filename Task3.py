"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

bangalore = []
within_bangalore =[]
for item in calls:
    if item[0][:5] == "(080)":
        bangalore.append(item[1]) # all the area codes here in bangalore
    if item[0][:5] == "(080)" and item[1][:5] == "(080)":
        within_bangalore.append(item[1])
    
total = len(bangalore)
local = len(within_bangalore)
val = (local/total)*100

area_code = set()
for item in bangalore:
    if item[0:2] =="(0":
        x = re.search(r"\b(\d+)", item)
        area_code.add(x.group())
    if item[0] == '7' or item[0] == '8' or item[0] == "9":
        area_code.add(item[0:4])
    if item[0:3] =="140":
        area_code.add("140")

codes = sorted(area_code)
print("The numbers called by people in Bangalore have codes:")
print('\n'.join(codes))
 
print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." %val)


'''    
area_code = set()
import re
for itemi in bangalore:
    if item[0:2] =="(0":
        str = "(08028) 1239739"
        x = re.search(r"\(\d+\)\$", str)
        print(x.group())
    
import re
str = "(08028) 1239739"
x = re.search(r"\b(\d+)", str)
print(x.group())

import re
str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())


'''
    
    

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.    
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
