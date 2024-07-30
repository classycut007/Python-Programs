print("Reverse Number")
num = int(input("Enter A Number: "))
n = 0
while num > 0:
    rem = num%10
    revrse = n*10 + rem
    num//=10
print("Reverse Number: ",revrse)