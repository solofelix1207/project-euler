#Problem 1 - Multiples of 3 and 5
#--------------------------------
# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

limit = int(input('\nEnter the number to begin: '))
limit_range = list(range(1,limit))

fin_list = []
fin_list1 = []

#print(limit_range)
for num in limit_range:
    num1 = num*3
    num2 = num*5
    while num1 < limit:
        fin_list.append(num1)
        break
    while num2 < limit:
        fin_list1.append(num2)
        break

print(f'The sum of the natural numbers below {limit} that are multiples of 3 or 5 is: {sum(set(fin_list + fin_list1))}')