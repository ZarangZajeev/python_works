allstudents=open("D:\\MY PC\\july_python_works\\file operation\\allstudents.txt",)
failedstudents=open("D:\\MY PC\\july_python_works\\file operation\\failed.txt")
all_students={line.rstrip("\n") for line in allstudents}
failed_students={line.rstrip("\n") for line in failedstudents}
passed_students=all_students.difference(failed_students)
print(passed_students)