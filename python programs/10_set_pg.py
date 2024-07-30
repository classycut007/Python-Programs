# Set Datatype:
#---> It not maintain sequence it show another order

# set = {10, 20, 30, 40, 50}
# print(set)
# set.update([50,60]) # Add value and same value replace in set
# print(set)
# set.remove(30)
# print(set) # remove the value in set


# Create set using list
# l = [10, 20, 30, 40]
# s = set(l)
# print("List: ",l)
# print("Set Using List: ",s)


#---------Frozenset Datatype----------

s = {10, 20, 30, 40}
f = frozenset(s)
print("set: ",s)
print(f)

fs=frozenset("akshay")
print(fs)