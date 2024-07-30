# x = int(input('Enter a number greater than 0: '))
# assert x > 0, "Wrong input entered"
# print("You entered:", x)


# Handeled Above the error using try and except block

num = int(input("Enter The Number Greater Than 0: "))
try:
    assert num>0
    print("You Entered: ",num)
except:
    print("Wrong Entered Number")
