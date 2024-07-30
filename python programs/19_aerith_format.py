num1 = int(input("Enter First Number: "))
num2= int(input("Enter Second Number: "))

print("The Addtion Of {} and {} Is {} ".format(num1,num2,num1+num2))
print("The Subtraction Of {} and {} Is {} ".format(num1,num2,num1-num2))
print("The Multiplication Of {} and {} Is {} ".format(num1,num2,num1*num2))
print("The Divsion Of {} and {} Is {} ".format(num1,num2,num1/num2))
print("The Module Of {} and {} Is {} ".format(num1,num2,num1%num2))

# eval() Function: 

number = eval(input("Enter An Expression: "))
print("Ans Is: ",round(number, 2))