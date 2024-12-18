class Figere:
    sides_count = 0
    __sides = 0
    __color = 0
    field = 0

    def get_color(self):
        return Figere.__color

    def __is_valid_color(self, r, g, b):
        self.r = 0
        self.g = 0
        self.b = 0

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)

    def __is_valid_sides(self):
        pass

    def sides(self):
        return self.__sides

    def __len__(self):
        sum = Figere.sides() + Figere.sides()
        return sum

    def set_sides(self, *new_sides):
        if new_sides != sides_count:
            self.new_sides = sides_count
        return self.__sides = new_sides



class Circle(Figere):
    sides_count = 1
    __radius =0

    def get_square(self):
        return 0

class Triangle(Figere):
    sides_count = 3

    def get_square(self):
        return 0

class Cube(Figere):
    sides_count = 12

    def get_square(self):
        return 0

