class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hola, mi nombre es {self.name} y tengo {self.age}")

person1 = person("ana", 30)
person2 = person("juan", 30)

person1.greet()

