#1
dog={}
print(type(dog))

#2
dog["name"]="Akiles"
dog["color"]="Golden"
dog["breed"]="Labrador"
dog["legs"]=4
dog["age"]=8
print(dog)

#3
student={"first_name":"Unai", "last_name":"Guerra Matas", "gender":"Male", "Age":20,"Marital status":"Single","Skills":["Python"],"Country":"Spain","City":"Toledo","Address":"Villasequilla"}
print(student)

#4
print(len(student))

#5
print(student["Skills"])
print(type(student["Skills"]))

#6
student["Skills"].append("SQL")
print(student["Skills"])

#7
print(student.keys())

#8
print(student.values())

#9
student_tp=student.items()
print(student_tp)

#10
student.pop("Skills")
print(student)

#11
del student 

