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
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
diff_phone_nums = []

#use not in iteration to append unique phone numbers to list, then print length of list

for num in texts:
    if num[0] not in diff_phone_nums:
        diff_phone_nums.append(num[0])
    if num[1] not in diff_phone_nums:
        diff_phone_nums.append(num[1])
for num in calls:
    if num[0] not in diff_phone_nums:
        diff_phone_nums.append(num[0])
    if num[1] not in diff_phone_nums:
        diff_phone_nums.append(num[1])


print(f"There are {len(diff_phone_nums)} different phone numbers in the records")