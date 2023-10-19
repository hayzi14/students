q = open ('students_new.txt','r',encoding = 'utf-8')

students = []
for student in q:
    p = student.split(';')
    id = int(p[0])
    var = int (p[2])
    group =(p[3])
    name = p[1] 
    students.append({'id': id, 'full_name': name,'var' : var, 'group' : group})   
for student in students:
    print(student)
q.close()
