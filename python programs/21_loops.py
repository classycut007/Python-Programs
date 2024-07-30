# While loop 
#-----------------------

# ---print 1 to 10

# i = 1
# while i<=10:
#     print(i,end=" ")
#     i+=1


# ----- print 10 to 1

# i = 10
# while i>=1:
#     print(i,end=" ")
#     i-=1


#----print even number between 1 to 100

# i=1
# while i<=100:
#     if(i%2==0):
#         print(i,end=" ")
#     i+=1


#----print Odd number between 1 to 100

# i=1
# while i<=100:
#     if(i%2!=0):
#         print(i,end=" ")
#     i+=1



# For in loop 
#-----------------------

#----- display and find sum of list

# l = [10, 20, 30, 40, 50]
# sum = 0
# for i in l:
#     sum+=i
# print("Sum Is: ",sum)


#--- sum of odd numbers from the list

l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    if(i%2==0):
        sum+=i
print("Sum Is: ",sum)

#--- sum of even numbers from the list

l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    if(i%2!=0):
        sum+=i
print("Sum Is: ",sum)