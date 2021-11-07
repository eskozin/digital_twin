# имитационная модель использования личного транспорта
import numpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import pylab
import pandas as pd

class Vehicle:
    # автомобиль с его параметрами
    def __init__(self, type, some_other_parameter1, some_other_parameter2):
        self.type = type
        self.some_other_parameter1 = some_other_parameter1
        self.some_other_parameter2 = some_other_parameter2

class Generator:
    # создаем функцию генерации массива с нормальным распределением с медианой median, стандартным отклонением deviation
    # и кол-вом значений number_of_gen
    def __init__(self, number_of_gen, median, deviation):
        self.number_of_gen = number_of_gen
        self.median = median
        self.deviation = deviation


    def array_generation(self):
        array = []
        for i in range(self.number_of_gen):
            array.append(np.random.normal(self.median, self.deviation))
        return array

class Hystogram:
    # создаем функцию показа гистограммы
    def __init__(self, array):
        self.array = array

    def draw_hystogram(self):
        pylab.hist(self.array, edgecolor='white')
        pylab.show()

class Excel:
    # создаем функцию выгрузки в excel файл
    # filepath = r'C:\Users\Evgeniy\desktop\{}.xlsx'.format('array')
    def __init__(self, array, filepath):
        self.array = array
        self.filepath = filepath

    def upload_to_excel(self):
        df = pd.DataFrame(self.array)
        df.to_excel(self.filepath, index=False)

#parameter1 = Generator(365,20,2).array_generation()
#parameter2 = Generator(365,20,2).array_generation()

#c = Hystogram(parameter1)
#c.draw_hystogram()

#vehicle1 = Vehicle('BMW', parameter1, parameter2)

# # создаем из исходного массива массив mileage_growth с нарастающей наработкой
# # для начала объявляем массив с нулями и преобразуем его в вектор-столбец
# mileage_growth = (np.zeros(trials, dtype=int))[:, np.newaxis]
# amount_of_maintenance = (np.zeros(trials, dtype=int))[:, np.newaxis]
#
# maintenance_count = 1
# for i in range(1, len(mileage_per_period)):
#     mileage_growth[i] = mileage_per_period[i] + mileage_growth[i - 1]
#     # посчитаем количество ТО за период,
#     if mileage_growth[i] >= maintenence_periodicity * maintenance_count:
#         maintenance_count += 1
#         amount_of_maintenance[i] = 1
#     else:
#         amount_of_maintenance[i] = 0
#
# # print(mileage_growth)
# # print(amount_of_maintenance)
# # сколько значений масива больше 0?
# print(np.count_nonzero(amount_of_maintenance > 0))
# # есть ли в массиве значения больше 0
# print(np.any(amount_of_maintenance > 0))
# # есть ли в массиве значение больше 800, но меньше 2000?
# print(np.sum((mileage_growth > 800) & (mileage_growth < 2000)))






