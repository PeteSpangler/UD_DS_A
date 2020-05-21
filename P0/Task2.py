
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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# morph given list into dictionary for easier access / indexing
# assisted by https://www.geeksforgeeks.org/python-dictionary/
def total_time(call):
    screen_time = {}
    for details in call:
        if details[0] not in screen_time.keys():
            screen_time[details[0]] = details[-1]
        
        else:
            screen_time.update({details[0]: int(screen_time[details[0]]) + int(details[-1])})
        
        if details[1] not in screen_time.keys():
            screen_time[details[1]] = details[-1]

        else:
            screen_time.update({details[1]: int(screen_time[details[1]]) + int(details[-1])})

    all_screen_time = [int(i) for i in screen_time.values()]
    max_time = max(all_screen_time)

    for n in screen_time.keys():
        if screen_time[n] == max_time:
            phone_hog = n
            break
    return phone_hog, max_time

phone_num, on_phone = total_time(calls)

print(f"{phone_num} spent the longest time, {on_phone} seconds, on the phone during September 2016.")