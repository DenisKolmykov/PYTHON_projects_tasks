"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    mass_1kwm = 25
    thick = 0.05

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        return

    def mass(self):
        res_mass = self.__length * self.__width * self.mass_1kwm * self.thick
        # return f'масса асфальта при длине дороги = {self.__length}м, ' \
        #       f'шириной {self.__width}м = {res_mass} кг = {res_mass / 1000}тн' \
        #       f'\nпри весе 1 м2 асфальта толщиной 1см = {self.mass_1kwm}кг' \
        #       f'\nи толщине асфальтового покрытия = {self.thick}м'
        return res_mass

    def __str__(self):
        return f'масса асфальта при длине дороги = {self.__length}м,' \
               f'шириной {self.__width}м = {self.mass()} кг = {self.mass() / 1000}тн' \
               f'\nпри весе 1 м2 асфальта толщиной 1см = {self.mass_1kwm}кг' \
               f'\nи толщине асфальтового покрытия = {self.thick}м'


length = 5000
width = 20

print('Дорога №1')
road_1 = Road(length, width)
# road_1_mass = road_1.mass() # записываем массу, если дальше вдруг надо будет использовать
print(road_1)  # печать через метод __str__

# если не прописывать в классе(методе класса) вывод на печать
# --------
# print(
#    f'масса асфальта при длине дороги = {length}м, шириной {width}м = '
#    f'{road_1.mass()} кг = {road_1.mass() / 1000}тн')
# print(f'при весе 1 м2 асфальта толщиной 1см = {road_1.mass_1kwm}кг')
# print(f'и толщине асфальтового покрытия = {road_1.thick}м')
# --------

print()
print('Дорога №2')
road_2 = Road(length, width)
road_2.mass_1kwm = 50
road_2.thick = 0.1
print(road_2)
