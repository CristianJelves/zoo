class Animal(object):
    def __init__(self, nombre: str, edad, salud: int, felicidad: int):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
        self.especies = str()

    def display_info(self):
        s = f"Esta {self.especies} es nombrado {self.nombre}, esta {self.salud}, y es {self.felicidad}."
        return s

    def feed(self):
        self.salud += 10
        self.felicidad += 10


class Lion(Animal):
    def __init__(self, nombre: str, edad="desconocida", salud: int = 3, felicidad: int = 3):
        super().__init__(nombre, edad, salud, felicidad)

class Tiger(Animal):
    def __init__(self, nombre: str, edad="desconocida", salud: int = 4, felicidad: int = 5):
        super().__init__(nombre, edad, salud, felicidad)

class Bear(Animal):
    def __init__(self, nombre: str, edad="desconocida", salud: int = 2, felicidad: int = 10, color: str="cafe"):
        super().__init__(nombre, edad, salud, felicidad)
        self.color = color


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()