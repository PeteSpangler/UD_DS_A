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
#Part A solution
#Use list iteration technique from Task 1 to create area code list
def list_of_codes(bgcallers):
    area_codes = []

    for users in bgcallers:

        receiver = users[1]

        if receiver[:2] == '(0':
            area_codes.append(receiver[1:4])

        if receiver[:3] == '140':
            area_codes.append('140')

        if receiver[0] == '7' or receiver[0] == '8' or receiver[0] == '9':
            area_codes.append(receiver[:4])

    unique_code = sorted(list(set(area_codes)))

    return unique_code


# Part B solution

def percentage_receiver(bgcallers):
    bg_pickup = [user[1] for user in bgcallers if user[1][:5] == '(080)']

    percentage = len(bg_pickup) / len(bgcallers) * 100

    return percentage


bg_callers = [[details[0], details[1]] for details in calls if details[0][:5] == '(080)']

unique_codes = list_of_codes(bg_callers)

print("The numbers called by people in Bangalore have codes:")
for ph_code in unique_codes:
    print(ph_code)

percentages = percentage_receiver(bg_callers)
print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentages))