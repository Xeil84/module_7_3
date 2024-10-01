class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors
        print(f'Жилой комплекс "{self.name}", этажей {self.floors}')

    def go_to(self, new_floor):
        if self.floors >= new_floor > 0:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)