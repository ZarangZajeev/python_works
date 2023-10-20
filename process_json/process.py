from json import load

# with open("D:\MY PC\july_python_works\process_json\students.json","r") as f:
#     data=load(f)

# print(len(data))

student=open("D:\\MY PC\\july_python_works\\process_json\\students.json")
data=load(student)
print(len(data))

name=[n.get("name") for n in data ]
print(name)

student.close()