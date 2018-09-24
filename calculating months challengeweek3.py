
r = 0.05 / 12
n = 20 * 12
P = 10000000
A = P * r * (1+r)**n / ((1+r)**n - 1)

outstanding = P
month = 0

for i in range(240):
    month = month + 1
    interest = outstanding * r
    principal = A - interest
    outstanding = outstanding - principal
if outstanding<=0:
    print('number of months',month)
