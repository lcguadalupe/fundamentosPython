# function input -> retorna string
name = input('como te llamas: \n')
age = int (input('cuantos años tienes? \n'))
future = int(input('cuantos años mas? \n'))

print("hola " + name)
print("en " + str (future) + " años tendras " + str(age + future))

#format strings
"""
    hola pochu, en 3 años tendras 24
"""
text_complete = "hola {}, en {} años tendras {} años"
print(text_complete.format(name, future, age + future))

print(f"hola {name}, en {future} años tendras {age + future} años")