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

    def __len__(self):
        return self.floors

    def __str__(self):
        return (f'Название: "{self.name}", кол-во этажей: {self.floors}')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))