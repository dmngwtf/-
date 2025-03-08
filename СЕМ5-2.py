import numpy as np
from math import pi, sqrt

# Функции для полосового фильтра
def f2w(f):
    return 2.0 * pi * f

def calculate_bandpass_components(f0, fl, fh, Z0):
    """Расчет компонентов полосового фильтра"""
    L = (sqrt(Z0**2 * f2w(f0)**2 * (2*f2w(fh)**2 - f2w(fl)**2 - f2w(f0)**2) /
         ((f2w(fh)**2 - f2w(fl)**2)**2 * (f2w(f0)**2 - f2w(fl)**2))))
    C1 = 2.0 / L / (f2w(fh)**2 - f2w(fl)**2)
    C2 = 1.0 / (f2w(fl)**2 * L)
    return L, C1, C2

# Функция для низкочастотного фильтра Т-типа
def calculate_t_type_lpf_components(fc, Z0):
    """Расчет компонентов НЧ фильтра Т-типа"""
    L_total = Z0 / (pi * fc)
    L_each = L_total / 2
    C = 1 / (pi * Z0 * fc)
    return L_each, C

# Ввод данных для полосового фильтра
print("\n=== Расчет полосового фильтра ===")
f = float(input('Опорная частота сигнала (f), Гц: '))
T = float(input('Временной интервал (T), с: '))
n = int(input('Число временных отсчетов (n): '))
fl = float(input('Нижняя граничная частота (fl), Гц: '))
fh = float(input('Верхняя граничная частота (fh), Гц: '))
f0 = (fl + fh) * 0.5

# Ввод данных для НЧ фильтра
print("\n=== Расчет низкочастотного фильтра Т-типа ===")
fc = float(input('Частота среза (fc), Гц: '))

# Ввод трех значений характеристического сопротивления
Z0_values = [
    float(input('Характеристическое сопротивление 1 (Z0_1), Ом: ')),
    float(input('Характеристическое сопротивление 2 (Z0_2), Ом: ')),
    float(input('Характеристическое сопротивление 3 (Z0_3), Ом: '))
]

# Расчет и вывод для полосового фильтра
print("\n=== Результаты для полосового фильтра ===")
print(f"Центральная частота (f0): {f0:.2e} Гц")
print("Формулы для полосового фильтра:")
print("L = sqrt(Z0² * (2πf0)² * (2*(2πfh)² - (2πfl)² - (2πf0)²) / (((2πfh)² - (2πfl)²)² * ((2πf0)² - (2πfl)²)))")
print("C1 = 2 / (L * ((2πfh)² - (2πfl)²))")
print("C2 = 1 / ((2πfl)² * L)")
print("=======================================")

for i, Z0 in enumerate(Z0_values, 1):
    L, C1, C2 = calculate_bandpass_components(f0, fl, fh, Z0)
    print(f'\nПараметры для Z0_{i} = {Z0} Ом:')
    print(f'L = {L:.6e} Гн')
    print(f'C1 = {C1:.6e} Ф')
    print(f'C2 = {C2:.6e} Ф')

# Расчет и вывод для НЧ фильтра Т-типа
print("\n=== Результаты для низкочастотного фильтра Т-типа ===")
print(f"Частота среза (fc): {fc:.2e} Гц")
print("Формулы для НЧ фильтра Т-типа:")
print("L_total = Z0 / (π * fc)")
print("L1 = L2 = L_total/2")
print("C = 1 / (π * Z0 * fc)")
print("=======================================")

for i, Z0 in enumerate(Z0_values, 1):
    L_each, C = calculate_t_type_lpf_components(fc, Z0)
    print(f'\nПараметры для Z0_{i} = {Z0} Ом:')
    print(f'L1 = L2 = {L_each:.6e} Гн')
    print(f'C = {C:.6e} Ф')
