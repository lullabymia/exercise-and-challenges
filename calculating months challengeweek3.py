
r = 0.05 / 12
P = 3000000
A = 85000

outstanding = P

month = 0
while outstanding >= 0:
    month = month + 1
    interest = outstanding * r
    principal = A - interest
    outstanding = outstanding - principal
    row = '{0:04d}	{1:.2f}	{2:7.2f}	{3:.2f}	{4:.2f}'.format(month, A, interest, principal, outstanding)
    print(row)
    if outstanding < 0:
        print('months paid off:', month)
