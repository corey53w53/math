#Corey Wang Discrete 6-6 Homework
from random import *
num_sims=10000000
num_rounds_sum=0
hanks_wins=0
for _ in range(num_sims):
    hanks_chips=4
    teds_chips=2
    num_rounds=0
    while hanks_chips and teds_chips:
        if randint(0,2):
            hanks_chips-=1
            teds_chips+=1
        else:
            hanks_chips+=1
            teds_chips-=1
        num_rounds+=1
    if hanks_chips:
        hanks_wins+=1
    num_rounds_sum+=num_rounds
print(f'Average number of rounds in {num_sims} trials: {num_rounds_sum/num_sims}')
print(f'Hank\'s wins: {hanks_wins}')
print(f'Ted\'s wins: {num_sims-hanks_wins}')


# def ncr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return (numer//denom)
# third_counter=2
# half_counter=0
# sum=0
# while half_counter<=7:
#     third=(1/3)**third_counter
#     half=(1/2)**half_counter
#     choose=ncr(third_counter,half_counter)
#     sum+=(third*half*choose)
#     third_counter+=1
#     half_counter+=1
# print(sum)