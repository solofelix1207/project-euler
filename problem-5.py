#Problem 5 - 
def LeastCommonMultiple(var):
    #Loop through all the multiples of the biggest number
    i = 1
    checkmultiple = []
    while   len(checkmultiple) != var-1:
        checkmultiple.clear()    #clear the checkmultiple list of the previous entry
        x = var*i    #get the multiples of 20
        #check if x is divisible by all the numbers between 1 and 19 without a remainder
        #loop through 1-19
        for j in range(1,var):   #looping through the other lower numbers
            if x%j == 0:       #check each of the these numbers against the multiple of 20 for even divisibility
                checkmultiple.append(1)   #if evenly divisible, append the checkmultiple list with 1 if not skip
            elif x%j != 0:     #if not skip
                continue
        if len(checkmultiple) == var-1:   #when you hit the LCM all 19 will record 1 at that point, return x
            return x
        i+=1         #until then, keep looping
            

print(LeastCommonMultiple(20))