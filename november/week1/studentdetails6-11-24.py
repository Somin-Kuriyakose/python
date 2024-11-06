student={"Name":"Mrunal","Roll no":"34","Reg no":"MCA3456","Dept":"MCA","Semester":"1","Marks":{"MFC":19,"Data Structure":18,"DFCA":12,"Software Engineering":18,"Python":15}}
total_marks=sum(student["Marks"].values())
if total_marks>=90:
    Grade="A"
elif total_marks>=82:
    Grade="B"
elif total_marks>=75:
    Grade="C"
elif total_marks>=60:
    Grade="D"
elif total_marks>=50:
    Grade="F"
else:
    student.pop("Roll no")

student["total_marks"]=total_marks
student["grade"]=Grade
print("Updated student dictionary:")
for key,value in student.items():
    if key=="marks":
        print(f"{key}:{value}")
    else:
        print(f"{key}:{value}")
