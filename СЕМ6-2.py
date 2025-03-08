import numpy as np
import matplotlib.pyplot as plt

# Параметры ФНЧ Т-типа
L = 10e-6  # Индуктивность, 10 мкГн
C = 1e-9   # Общая ёмкость, 1 нФ (C/2 + C/2)
G = 1 / 50  # Проводимость, G = 1/R, R = 50 Ом (для Z0_1)
f = np.logspace(2, 7, 1000)  # Диапазон частот от 10 Гц до 1 МГц

# Характеристические сопротивления
Z0_1 = 50   # Ом
Z0_2 = 100  # Ом
G2 = 1 / Z0_2  # Проводимость для Z0_2

# Частотная зависимость импеданса
def lowpass_t_filter_response(f, L, C, G, Z0):
    w = 2 * np.pi * f
    ZL = 1j * w * L
    ZC = 1 / (1j * w * C)
    YG = G + 1 / Z0  # Общая проводимость с учётом нагрузки
    Z_parallel = 1 / (YG + 1 / ZC)  # Параллельная ветвь
    H = Z_parallel / (ZL + Z_parallel)  # Коэффициент передачи
    return H

# Расчёт для двух Z0
H1 = lowpass_t_filter_response(f, L, C, G, Z0_1)
H2 = lowpass_t_filter_response(f, L, C, G2, Z0_2)

# Амплитуда и фаза
amp1 = np.abs(H1)
amp2 = np.abs(H2)
phase1 = np.angle(H1, deg=True)
phase2 = np.angle(H2, deg=True)

# Построение графиков
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.semilogx(f / 1e3, amp1, label=f'Z0 = {Z0_1} Ом')
plt.semilogx(f / 1e3, amp2, label=f'Z0 = {Z0_2} Ом')
plt.title('Частотные характеристики ФНЧ Т-типа')
plt.xlabel('Частота, кГц')
plt.ylabel('Амплитуда |H(f)|')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.semilogx(f / 1e3, phase1, label=f'Z0 = {Z0_1} Ом')
plt.semilogx(f / 1e3, phase2, label=f'Z0 = {Z0_2} Ом')
plt.title('Фазовые характеристики ФНЧ Т-типа')
plt.xlabel('Частота, кГц')
plt.ylabel('Фаза, градусы')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()