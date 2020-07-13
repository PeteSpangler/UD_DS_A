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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# change given list into dictionary for easier access / indexing / not in iteration
# assisted by https://www.geeksforgeeks.org/python-dictionary/ 
def screen_time():
    call_time = {}
    for call in calls:
        if call[0] not in call_time:
            call_time[call[0]] = 0
        if call[1] not in call_time:
            call_time[call[1]] = 0
        call_time[call[0]] += int(call[3])
        call_time[call[1]] += int(call[3])
    long_call = ('None', 0)
    for num in call_time:
        if call_time[num] > long_call[1]:
            long_call = (num, call_time[num])
    return long_call

ph_num, time = screen_time()

print(f"{ph_num} spent the longest time, {time} seconds, on the phone during September 2016.")