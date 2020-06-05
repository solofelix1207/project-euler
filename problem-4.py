from time import time as t

print('Welcome to My Solution to Project Euler - Problem 4\n')
ndigi = int(input('Please enter number of digits (n): ')) 
start = t()     #record the start time
k1 = int('1' + ((ndigi-1)*'0'))    #use k1 and k2 to generate the start and end of the selected digits
k2 = int('1' + (ndigi*'0'))         #example for 2, this will be 100 to 1000 (range will correct it to 99)         

results = []   
palinum = []

for x in range (k1,k2):          #use this loop to generate the list of all the products of all the multiplications
    for y in range(k1,k2):
        results.append(x*y)

for num in results:
    num = str(num)   #convert to string so we can loop through
    l = int(len(num)/2)  #divide de length of the number by 2 and take only the whole number part if results is odd. 
    halfrange = []
    for h in range(l):         #if number is 5 characters we have 2. Now check first 2 elements and record it in the halfrange variable
        halfrange.append(num[h])
    otherhalf = []
    num2 = num[::-1]  #reverse the digits and do same as above. store the number i nhalfrange2 
    halfrange2 = []
    for k in range(l):
        halfrange2.append(num2[k])
    if halfrange == halfrange2:      #check for equality
        num = int(num)
        palinum.append(num)        #store the equal numbers 

palinum.sort()   #sort from lowest to highest and in below print statement, pick the last item which is the highest.
print(f'The largest palindrome made from the product of two {ndigi}-digit numbers is: {palinum[-1]}')
end = t()
print('Time taken: ' + str(round((end-start),2)) + ' seconds')
holder = input('\nPress ENTER to exit...')