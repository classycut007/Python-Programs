# String Datatype

# str = "Welcome To Akshaybhai"
# print(str)

# print(str[0]) #display 0th character

# print(str[3:7]) #display from 3rd to 6th characters

# print(str[11:]) #display from 11th character to end

# print(str[-1]) #display first character from the end

# print(str*2) # It Print Multi Time string


#---------Byte Datatype------------

# element = [10, 20, 30]
# # print(type(byte)) # List
# # Conver list into bytes datatype
# byte = bytes(element)
# print(type(byte))
# for i in byte:
#     print(i, end=" ")


#-----------ByteArray Datatype-----------

# element = [10, 20, 30]
# # Conver list into bytearray datatype
# byte = bytearray(element)
# print(type(byte))

# # Bytearray should be modified but byte not modifie values

# byte[0]=1 
# for i in byte:
#     print(i)


# -------------List Datatype ------------

# list = [1, 2, "akshay", 10, "abhi"]
# print(list)
# list[1]=20
# for i in list:
#     print(i,end=" ")
# print(list[-1]) # Dispaly last element
# print(list[2:]) # dispaly first two element ignore and after so all print


#---------Tuple Datatype----------

tuple = (1, 2, 3, "akshay")
print(type(tuple))
print(tuple)

# tuple[0]=10 //-----> Don't Modified tuple datatypes
for i in tuple:
    print(i)