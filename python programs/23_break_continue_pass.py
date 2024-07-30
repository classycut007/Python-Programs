# break


for i in range(5):
    if(i==3):
        break
    print(i)

# grp = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# search = int(input("Enter Element To Search Between 10 To 100: "))
# for element in grp:
#     if search == element:
#         print("Your ({}) Element Is Found".format(element))
#         break
#     else:
#         print("Your element Not there")




# Continue

# for i in range(5):
#     if(i==3):
#         continue
#     print(i)



# pass

num=[1,2,3,-4,-5,-6,-7,8,9]
for i in num:
    if(i>0):
        pass
    else:
        print(i,end=" ")