import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

horas = np.array([
    '05:00-06:00', '06:00-07:00', '07:00-08:00', '08:00-09:00', '09:00-10:00',
    '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00',
    '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00',
    '20:00-21:00'
])

x = np.arange(len(horas))

motocicleta = np.array([
    747.3333333, 2689.833333, 4820.5, 2963.666667, 2503.5, 2492.666667, 
    2709.166667, 2478.666667, 2490.166667, 2832.666667, 3011.833333, 
    3223.333333, 5033.666667, 5165.333333, 2834.833333, 1782.833333
])

passeio = np.array([
    5720.666667, 20841.83333, 33496.5, 28773.66667, 24910.16667, 23056.5, 
    23034.83333, 23821, 25559.5, 24991.83333, 25174, 27716, 34495.5, 
    34221.16667, 26690.33333, 17893.5
])

onibus = np.array([
    384.3333333, 805.1666667, 900.1666667, 724.6666667, 510.6666667, 
    385.8333333, 389, 416, 426.3333333, 384.5, 439.8333333, 523.3333333, 
    721.5, 715.6666667, 548.6666667, 309.8333333
])

cargas = np.array([
    787.1666667, 1471.833333, 1606.166667, 1849, 2016.5, 2034.166667, 
    1918.166667, 1528.5, 1594.333333, 1972, 2035.166667, 1859.333333, 
    1388, 941.5, 576.1666667, 423
])

x_smooth = np.linspace(x.min(), x.max(), 300)
motocicleta_smooth = make_interp_spline(x, motocicleta)(x_smooth)
passeio_smooth = make_interp_spline(x, passeio)(x_smooth)
onibus_smooth = make_interp_spline(x, onibus)(x_smooth)
cargas_smooth = make_interp_spline(x, cargas)(x_smooth)

plt.figure(figsize=(12, 8))
plt.plot(x_smooth, motocicleta_smooth, label='Motocicleta', linewidth=2)
plt.plot(x_smooth, passeio_smooth, label='Passeio', linewidth=2)
plt.plot(x_smooth, onibus_smooth, label='Ônibus', linewidth=2)
plt.plot(x_smooth, cargas_smooth, label='Cargas', linewidth=2)

plt.scatter(x, motocicleta, color='blue', s=50, zorder=5)
plt.scatter(x, passeio, color='orange', s=50, zorder=5)
plt.scatter(x, onibus, color='green', s=50, zorder=5)
plt.scatter(x, cargas, color='red', s=50, zorder=5)

plt.xticks(x, horas, rotation=45)
plt.legend(loc='upper left')
plt.title('Distribuição e fluxograma do Volume de Veículos por Modo e Hora')
plt.ylabel('Número de Viagens')
plt.tight_layout()
plt.grid(True)
plt.show()
