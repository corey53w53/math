from random import *
num_sims=100000
round_num_sum=0
hanks_wins=0
for _ in range(num_sims):
    hchips=4
    tchips=2
    num_rounds=0
    while hchips and tchips:
        if randint(1,3)==1:
            hchips+=1
            tchips-=1
        else:
            hchips-=1
            tchips+=1
        num_rounds+=1
    if tchips==0:
        hanks_wins+=1
    round_num_sum+=num_rounds
print(f'Average number of rounds in {num_sims} trials: {round_num_sum/num_sims}')
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