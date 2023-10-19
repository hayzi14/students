f = open('students_new.txt','r',encoding='utf-8')

students = []
for student in f :

        p = student.split(';')
        
        id = int(p[0])
        
        lastname = p[1]
        
        name = p[2]
        
        surname = p[3]
        
        var = int(p[4]
               
        group = int(p[5])
               
        students.append({'id':id,'lastname':lastname, 'name':name, 'surname':surname, 'variant':var, 'group':group})
    
f.close()

name = input('Имя студента:')
for student in students:
    if student['name'] == name:
        print(student)
