# 5.1. Write a program which repeatedly reads numbers until the user enters "done". 
# Once 'done' is entered, print out the total, count and average of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 4, 5, bad data, 7, and done.

num=0
tot=0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    fval = float(sval)
    num = num + 1
    tot = tot + fval
avg = tot/num

print('ALL DONE')
print(tot,num,avg)