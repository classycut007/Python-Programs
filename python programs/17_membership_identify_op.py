# Mmbership op:
# 1. in   2. Not in

hero=["shazam","spiderman","bat-man"]
for i in hero:
    print(i)

x = 100
list = [10, 20, 30, 40]
if(x not in list):
    print("X not is present in list")
else:
    print("X is Present in list")



# Identify Op:
# 1. is :- compare whether two objects are same or not.       
# 2. is not :- compare two objects either not same it return true

a=10;b=20
if(a is b):
    print("A and B is same")
else:
    print("A and B is not same")

a=[10,20]
b=[10,20]
if(a is b):
    print("A and B is not same identify")
else:
    print("A and B is same identify")
