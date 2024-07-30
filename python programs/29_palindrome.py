print("Check Palindrome Number Or Not")
num = int(input("Enter A Number: "))
n = 0
temp=num
while num > 0:
    rem = num%10
    revrse = n*10 + rem
    num//=10
if temp == revrse:
    print(temp,"Is Palindrome Number")
else:
    print(temp,"Is Not Palindrome Number")