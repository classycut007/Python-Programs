print("Check Number Armstrong Or Not")
num = int(input("Enter A Number: "))

sum = 0
temp = num
while temp > 0:
    d = temp%10
    sum+= d ** 3
    temp//=10

if sum == num:
    print(num,"Is Armstrong Number")
else:
    print(num,"Is Not Armstrong Number")