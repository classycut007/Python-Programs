# print("Check The Prime Or Not")
# num = int(input("enter the number: "))

# if num == 1:
#     print(num,"Is Not Prime Number")
# if num < 0:
#     print("Please Enter Greater Than 0")
# if num > 1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"Is Not Prime Number")
#             break
#     # Else is for loop block
#     else:
#         print(num,"Is Prime Number")



# prime between 1 to 100.

for i in range(1,101):
    if i > 1:
        for num in range(2,i):
            if i%num==0:
                break
        else:
            print(i, end = " ")