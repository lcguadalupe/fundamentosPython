
# diccionarios
# {"clave": "valor"}

teacher = {
    "name": "pochu",
    "l_name": "lopez",
    "phone": "3561126893",
    "groups": ["3A","3b"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3C")
teacher["phone"] = "2471332671"
teacher["city"] = "huam"
print(teacher)
