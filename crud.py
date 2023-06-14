students = []

def show_estudents():
    for student in students:
        print(student)

def add_student(student):
    students.append(student)

def remove_student(student):
    try:
        students.remove(student)
    except exception:
        print("no existe")

choice_text = ''' 
elige una opcion:
    1 - insertar
    2 - mostrar
    3 - eliminar
    4 - salir
'''
while True:
    choice = int(input(choice_text))
    if choice == 1:
        student = input("ingresa student:\n")
        add_student(student)
    elif choice == 2:
            show_estudents()
    elif choice == 3:
        student = input("ingresa student a eliminar: \n")
        remove_student(student)
    elif choice == 4:
        break
    else:
        print('incorrect option!')    
