first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
third = int(input("Enter Third Number: "))

if(first%2==0 or second%2==0 or third%2==0):
    print("Please Enter All Numbers In Odd")
elif(first >= second and first >= third):
    print(first," Is Maximum Number.")
elif(second>=first and second>=third):
    print(second," Is Maximum Number")
else:
    print(third," Is Maximum Number")