# First you import the sys class after run the program

import sys
# n = len(sys.argv)
# args = sys.argv
# print("No Of Command Line Argument: ",n)
# print("The argument are: ",args)
# print("The Argument One By One: ")
# for a in args:
#     print(a,sep=",")


# ----Sum of two numbers using command line argument
# sum=int(sys.argv[1]) + int(sys.argv[2])
# print("Sum Is:",sum)


#----- Arithmetic operations usind cmd

# print("The Addtion Is: ",int(sys.argv[1])+int(sys.argv[2]))
# print("The Subtraction Is: ",int(sys.argv[1])-int(sys.argv[2]))
# print("The Multiplication Is: ",int(sys.argv[1])*int(sys.argv[2]))
# print("The Divsion Is: ",int(sys.argv[1])/int(sys.argv[2]))
# print("The Module Is: ",int(sys.argv[1])%int(sys.argv[2]))


#------ sum of only even numbers using cmd args

args = sys.argv[1:]
print("Argument is: ",args)
sum = 0


for s in args:
    x=int(s)
    if(x%2==0):
        sum+=x
print("Even Number Sum Is: ",sum)

