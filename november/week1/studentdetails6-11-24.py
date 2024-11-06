student={}
student["Name"]=input("Enter the name:")
student["Roll Number"]=input("Enter the roll number:")
student["Register Number"]=input("Enter the register number:")
student["Department"]=input("Enter the department:")
student["Semester"]=input("Enter the semester:")
print("Student details: ",student)
print()

student['total mark']=int(input("Enter the total mark out of 100:"))
print()
print("Student details after adding total mark:",student)
print()

if student['total mark']>=90:
    student['grade']='A'
    
elif student['total mark']>=82:
    student['grade']='B'
    
elif student['total mark']>=60:
    student['grade']='C'
    
elif student['total mark']>=50:
    student['grade']='p'
else:
    student['grade']='F'
print("Student details after adding grade:",student)
print()

student.pop('Roll Number')
print("Student details after deleting roll number:",student)


