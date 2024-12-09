import matplotlib.pyplot as plt

# Datos originales
x = [0.1, 3.1, 6.1, 9.1, 12.1, 15.1]
y = [4.5521, 121.5921, 205.5543, 256.0561, 272.8694, 256.491]

# Datos interpolados
t_values = [0.1, 0.725, 1.35, 1.975, 2.6, 3.225, 3.85, 4.475, 5.1, 5.725, 6.35, 6.975, 7.6, 8.225, 8.85, 9.475, 10.1, 10.725, 11.35, 11.975, 12.6, 13.225, 13.85, 14.475, 15.1]
h_values = [4.5521, 31.6539, 57.3246, 81.5652, 104.3752, 125.7530, 145.6959, 164.2007, 181.2635, 196.8802, 211.0465, 223.7585, 235.0123, 244.8050, 253.1344, 259.9992, 265.3996, 269.3370, 271.8150, 272.8386, 272.4153, 270.5551, 267.2702, 262.5761, 256.4910]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(t_values, h_values, label="Interpolación de Newton", color='blue')
plt.scatter(x, y, color='red', label="Datos Originales")
plt.xlabel("t (s)")
plt.ylabel("h (m)")
plt.title("Interpolación de Newton")
plt.legend()
plt.grid(True)
plt.show()
