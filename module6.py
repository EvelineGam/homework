import math

class Figure:
    sides_count = 0
    
    def __init__(self, color, side):
        self.__sides = list(side)
        self.__color = list(color)
        filled = False
        
    def get_color(self):
        return self.__color
        
    def __is_valid_color(self, r, g, b):
        color = [r, g, b]
        for i in color:
            return (0 <= i <= 255 and
                    isinstance(i, int))
            
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            filled = True
            return self.__color
            
    def __is_valid_sides(self, *sides):
        for side in sides:
            return side > 0 and isinstance(side, int) and len(sides) == sides_count
            
    def get_sides(self):
        return self.__sides
        
    def __len__(self):
        return sum(self.__sides)
        
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
            return self.__sides

class Circle(Figure):
    sides_count = 1
    
    def __init__(self, color, *side):
        self.side = self.__is_valid_count(side)
        super().__init__(color, self.side)
        self.__radius = int(self.side[0])/ 2 / math.pi
        
    def __is_valid_count(self, side):
        if len(side) != self.sides_count:
            return 1
        return side
        
    def get_square(self):
        return math.pi * self.__radius ** 2
            
class Triangle(Figure):
    sides_count = 3
    
    def __init__(self, color, *sides):
        self.sides = self.__is_valid_count(sides)
        super().__init__(color, self.sides)
        
    def __is_valid_count(self, sides):
        if len(sides) != self.sides_count:
            return [1] * self.sides_count
        else:
            return sides
        
    def get_square(self):
        p = sum(self.sides) / 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
        
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.sides = self.__is_valid_count(sides)
        super().__init__(color, self.sides)
        
    def __is_valid_count(self, sides):
        if len(sides) == 1:
            return sides * self.sides_count
        return [1] * self.sides_count
        
    def get_volume(self):
        return self.sides[0] ** 3
        
if __name__ == '__main__':
    
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    triangle =Triangle((170, 159, 35), 3, 2)
    
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)#Не изменится
    print(cube1.get_color())
    triangle.set_color(305, 56, 87)
    print(triangle.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())
    triangle.set_sides(3, 4)
    print(triangle.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
    
    # Проверка площади треугольника:
    print(triangle.get_square())
    
    #Проверка площади круга:
    
    