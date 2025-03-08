import numpy as np
import matplotlib.pyplot as plt

# Параметры ФНЧ Т-типа
L = 10e-6  # Индуктивность, 10 мкГн
C = 1e-9   # Ёмкость, 1 нФ
f = np.linspace(0, 5e6, 1000)  # Диапазон частот

# Характеристические сопротивления
Z0_1 = 50  # Ом
Z0_2 = 100  # Ом

# Частотная зависимость импеданса
def lowpass_t_filter_response(f, L, C, Z0):
    w = 2 * np.pi * f
    ZL = 1j * w * L
    ZC = 1 / (1j * w * C)
    Z_series = ZL + ZL  # Две индуктивности
    Z_parallel = 1 / (1 / ZC + 1 / Z0)
    H = Z_parallel / (Z_series + Z_parallel)  # Коэффициент передачи
    return H

# Расчёт для двух Z0
H1 = lowpass_t_filter_response(f, L, C, Z0_1)
H2 = lowpass_t_filter_response(f, L, C, Z0_2)

# Амплитуда и фаза
amp1 = np.abs(H1)
amp2 = np.abs(H2)
phase1 = np.angle(H1, deg=True)
phase2 = np.angle(H2, deg=True)

# Построение графиков
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(f / 1e6, amp1, label=f'Z0 = {Z0_1} Ом')
plt.plot(f / 1e6, amp2, label=f'Z0 = {Z0_2} Ом')
plt.title('Частотные характеристики ФНЧ Т-типа')
plt.xlabel('Частота, МГц')
plt.ylabel('Амплитуда |H(f)|')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f / 1e6, phase1, label=f'Z0 = {Z0_1} Ом')
plt.plot(f / 1e6, phase2, label=f'Z0 = {Z0_2} Ом')
plt.title('Фазовые характеристики ФНЧ Т-типа')
plt.xlabel('Частота, МГц')
plt.ylabel('Фаза, градусы')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()