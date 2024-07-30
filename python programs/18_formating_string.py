# string
str = "welcome"
print("hello %s"%str)
print("hello %20s"%str)

# Float

n = 123.34567
print("Numbr is: %f"%n)
print("Number is: %8.2f"%n)

# format style:

n1,n2,n3=10,20,30
# print("Number1: {0}, number2: {1}, Number3: {2}".format(n1,n2,n3))
print("Number1: {2}, number2: {0}, Number3: {1}".format(n1,n2,n3)) # Swapping In One Line

name="akshay";salary=15000.0055
print("Name: {0} And Your Salary: {1}".format(name,salary))

# Second way asign format 
print("Hello %s,Your salary: %8.3f"%(name,salary)) 