numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

information = {"nombre": "luna",
               "Apellido": "velez",
               "Altura": 1.60,
               "Edad": 20}
print(information)

del information["Edad"]
print(information)
claves = information.keys()
print(claves)

values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}
print(contacts["Carla"])