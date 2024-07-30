print("-------MarkSheet-------")
name = str(input("Enter Student Name: "))
no = int(input("Enter RollNo: "))
print("\n----Enter The Marks Of Subjects-----\n")
python = int(input("Python: "))
j2ee = int(input("J2EE: "))
cs = int(input("Cyber Security: "))
total=python+j2ee+cs
percentage=total/3

print("Student Name: ",name)
print("Roll No: ",no)
print("Python: ",python)
print("J2EE:",j2ee)
print("Cyber Security: ",cs,"\n----------------------")
print("Total Marks: ",total)
print("Percenatage: ",round(percentage, 2))