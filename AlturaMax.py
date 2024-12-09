import numpy as np

# Datos de vuelo
t = np.array([0.1, 3.1, 6.1, 9.1, 12.1, 15.1])
h = np.array([4.5521, 121.5921, 205.5543, 256.0561, 272.8694, 256.4919])

# Calcular las diferencias divididas
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef[0, :]

# Construir el polinomio de Newton
def newton_poly(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Derivada del polinomio de Newton
def newton_poly_derivative(coef, x_data, x):
    n = len(x_data) - 1
    p_deriv = 0
    for k in range(1, n + 1):
        term = coef[n]
        for j in range(n, n - k, -1):
            term *= (x - x_data[j - 1])
        p_deriv += term
    return p_deriv

# Método de Newton-Raphson para encontrar el máximo
def newton_raphson(coef, x_data, x0, tol=1e-4, max_iter=100):
    x = x0
    iteraciones = []
    for i in range(max_iter):
        fx = newton_poly_derivative(coef, x_data, x)
        fpx = -9.81  # La segunda derivada es constante y negativa
        x_new = x - fx / fpx
        iteraciones.append((i + 1, x, fx, x_new))
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x, iteraciones

# Calcular los coeficientes del polinomio de Newton
coef = divided_diff(t, h)

# Inicializar x0 y encontrar el máximo
x0 = 7  # Un valor inicial razonable
t_max, iteraciones = newton_raphson(coef, t, x0)
h_max = newton_poly(coef, t, t_max)

print(f"El tiempo en el que el dron alcanza la altura máxima es t = {t_max:.4f} s")
print(f"La altura máxima del dron es h = {h_max:.4f} m")

# Mostrar tabla de iteraciones
print("\nIteraciones:")
print("Iteración | t        | h'(t)    | t_nueva")
for it in iteraciones:
    print(f"{it[0]:9} | {it[1]:.4f} | {it[2]:.4f} | {it[3]:.4f}")
