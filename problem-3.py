#Problem 3 - Largest prime factor
#In Python using sympy 
#

from time import time as t
import sympy

start = t()
print(max(sympy.primefactors(600851475143)))

end = t()

print(f'time taken {round((end-start),2)} seconds')
