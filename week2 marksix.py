import random
i=1
list=list(range(1,50))
while i>0:
    a=random.choice(list)
    print(a)
    list.remove(a)
    i=i+1
    if i==8:
        break