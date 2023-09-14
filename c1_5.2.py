# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

list_collector = []
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        ival = int(sval)
    except:
        print('Invalid input')
        continue
    list_collector.append(ival)

smallest = None
largest = None
for num in list_collector:
    if largest is None:
        largest=num
    elif num > largest:
        largest = num
print("Maximum is", largest)

for num in list_collector:
    if smallest is None:
        smallest=num
    elif num < smallest:
        smallest = num
print("Minimum is", smallest)













