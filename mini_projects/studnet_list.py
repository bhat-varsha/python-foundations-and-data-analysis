students={}
def add_students():
    student_name=input("name of the student:")
    student_marks=int(input("marks of the student:"))
    if student_marks>85:
        student_grade="A"
    elif student_marks>70:
        student_grade="B"
    else :
        student_grade="C"
    print("grades",student_grade)
    students[student_name]={"marks":student_marks,"grade":student_grade}
    print(f'student {student_name} is added')
def show_student():
    for key,value in students.items(): #in dictionary key=student_name and value is grade and marks
        print(f'student={key}:final_marks={value["marks"]},final_grade={value["grade"]}')
while True:
    print("\n1.ADD STUDENTS\n2.SHOW STUDENT\n3.EXIT")
    print("\n1\n2\n3")
    choices=(input("choose one option here:"))
    if choices=="1":
        add_students()
    elif choices=="2":
        show_student()
    elif choices=="3":
        print("exit")
        break
    else:
        print("ivalid choices")
show_student()


