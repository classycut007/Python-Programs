# ----> First main thing is you decalre the function you use the "def" keyword.

# 1] With Argument, With Return

def sum(num1,num2):
    return(num1+num2)
ans = sum(10,20)
print("Sum Is:",ans)

# 2] with argument, no return

def sum(num1,num2):
    print("Sum Is:",num1+num2)
sum(10,20)


# 3] no argument, with return

def sum():
    num1=10;num2=20
    return(num1+num2)
print("Sum Is:",sum())

# 3] no argument, no return

def sum():
    num1=10;num2=20
    print("Sum Is:",num1+num2)
sum()