import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Установим параметры
fs = 1000  # Частота дискретизации (Гц)
t = np.linspace(0, 1, fs, endpoint=False)  # Временной вектор (1 секунда)

# Создаем сигнал с несколькими гармониками
f1, f2, f3 = 10, 20, 30  # Частоты гармоник
signal_input = (np.sin(2 * np.pi * f1 * t) + 
                0.5 * np.sin(2 * np.pi * f2 * t) + 
                0.3 * np.sin(2 * np.pi * f3 * t))

# 1. Фильтры для выделения одной гармоники
def create_and_apply_filter(filter_type, freq, signal_input, fs):
    nyquist = fs / 2
    if filter_type == 'low':
        wn = freq / nyquist
        b, a = signal.butter(5, wn, btype='low')
    elif filter_type == 'high':
        wn = freq / nyquist
        b, a = signal.butter(5, wn, btype='high')
    elif filter_type == 'band':
        wn = [freq[0]/nyquist, freq[1]/nyquist]
        b, a = signal.butter(5, wn, btype='band')
    
    return signal.filtfilt(b, a, signal_input)

# Низкочастотный фильтр (выделяем 10 Гц)
lowpass = create_and_apply_filter('low', 15, signal_input, fs)

# Высокочастотный фильтр (выделяем 30 Гц)
highpass = create_and_apply_filter('high', 25, signal_input, fs)

# Полосовой фильтр (выделяем 20 Гц)
bandpass_single = create_and_apply_filter('band', [15, 25], signal_input, fs)

# Полосовой фильтр для двух гармоник (10 и 20 Гц)
bandpass_double = create_and_apply_filter('band', [5, 25], signal_input, fs)

# 2. Прямоугольные импульсы и их фильтрация
def create_rectangular_pulses(periods, samples):
    t = np.linspace(0, 1, samples, endpoint=False)
    return signal.square(2 * np.pi * periods * t)

# Создаем прямоугольные импульсы с разным количеством периодов
rect_3 = create_rectangular_pulses(3, fs)    # 3 лепестка
rect_1 = create_rectangular_pulses(1, fs)    # 1 лепесток
rect_half = create_rectangular_pulses(0.5, fs)  # ½ лепестка

# Применяем низкочастотный фильтр к прямоугольным импульсам
rect_3_filtered = create_and_apply_filter('low', 10, rect_3, fs)
rect_1_filtered = create_and_apply_filter('low', 10, rect_1, fs)
rect_half_filtered = create_and_apply_filter('low', 10, rect_half, fs)

# Визуализация результатов
plt.figure(figsize=(15, 15))

# Графики для гармоник
plt.subplot(5, 2, 1)
plt.plot(t, signal_input)
plt.title('Исходный сигнал')
plt.grid()

plt.subplot(5, 2, 2)
plt.plot(t, lowpass)
plt.title('Низкочастотный фильтр (10 Гц)')
plt.grid()

plt.subplot(5, 2, 3)
plt.plot(t, highpass)
plt.title('Высокочастотный фильтр (30 Гц)')
plt.grid()

plt.subplot(5, 2, 4)
plt.plot(t, bandpass_single)
plt.title('Полосовой фильтр (20 Гц)')
plt.grid()

plt.subplot(5, 2, 5)
plt.plot(t, bandpass_double)
plt.title('Полосовой фильтр (10 и 20 Гц)')
plt.grid()

# Графики для прямоугольных импульсов
plt.subplot(5, 2, 6)
plt.plot(t, rect_3)
plt.title('Прямоугольные импульсы (3 лепестка)')
plt.grid()

plt.subplot(5, 2, 7)
plt.plot(t, rect_3_filtered)
plt.title('Отфильтрованные 3 лепестка')
plt.grid()

plt.subplot(5, 2, 8)
plt.plot(t, rect_1)
plt.title('Прямоугольные импульсы (1 лепесток)')
plt.grid()

plt.subplot(5, 2, 9)
plt.plot(t, rect_1_filtered)
plt.title('Отфильтрованный 1 лепесток')
plt.grid()

plt.subplot(5, 2, 10)
plt.plot(t, rect_half)
plt.title('Прямоугольные импульсы (½ лепестка)')
plt.grid()

plt.tight_layout()
plt.show()

# Спектральный анализ
def plot_spectrum(signal_data, title):
    freq = np.fft.fftfreq(len(signal_data), 1/fs)
    fft_result = np.abs(np.fft.fft(signal_data))
    plt.figure()
    plt.plot(freq[:len(freq)//2], fft_result[:len(freq)//2])
    plt.title(title)
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.grid()
    plt.show()

# Выводим спектры для исходного сигнала и отфильтрованных сигналов
plot_spectrum(signal_input, 'Спектр исходного сигнала')
plot_spectrum(lowpass, 'Спектр после низкочастотного фильтра')
plot_spectrum(highpass, 'Спектр после высокочастотного фильтра')
plot_spectrum(bandpass_single, 'Спектр после полосового фильтра (1 гармоника)')
plot_spectrum(bandpass_double, 'Спектр после полосового фильтра (2 гармоники)')