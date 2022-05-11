# serial number
#     Name
#     usn 
#     class
#     age

data_entry = int(input("enter the number of students "))
students_data = []
for i in range(data_entry):
    per_student = []
    serial_number = int(input("enter the serial number "))
    per_student.append(serial_number)
    student_name = input("enter the name ")
    per_student.append(student_name)
    student_usn = input("enter the student USN ")
    per_student.append(student_usn)
    student_marks = int(input("enter the student marks "))
    per_student.append(student_marks)

    students_data.append(per_student)



serial_number_output = int(input("enter the student serial number "))
print(students_data[serial_number_output])