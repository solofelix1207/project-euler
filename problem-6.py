

# final_numbers = []
# squares = []
raw_sum=0
sum_individual_squares =0

for i in range(1,101):
    raw_sum = raw_sum + i
    sum_individual_squares = sum_individual_squares + (i**2)

difference = (raw_sum**2) - sum_individual_squares 

print(difference)