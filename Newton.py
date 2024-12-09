def diferencias_divididas(x, y):
    n = len(y)
    coef = y.copy()
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
            
    return coef

def polinomio_newton(x, coef, t):
    n = len(coef)
    p = coef[0]
    for k in range(1, n):
        term = coef[k]
        for j in range(k):
            term *= (t - x[j])
        p += term
    return p

# Datos
x = [0.1, 3.1, 6.1, 9.1, 12.1, 15.1]
y = [4.5521, 121.5921, 205.5543, 256.0561, 272.8694, 256.491]

# Calcular los coeficientes del polinomio de Newton
coef = diferencias_divididas(x, y)

# Imprimir los coeficientes
print("Coeficientes del polinomio de Newton:")
for i, c in enumerate(coef):
    print(f"a{i} = {c}")

# Generar 25 puntos equidistantes en el rango de los datos proporcionados
import numpy as np
t_values = np.linspace(min(x), max(x), 25)
h_values = [polinomio_newton(x, coef, t) for t in t_values]

# Imprimir la tabla de valores
print("\nt(s)        h(m)")
for t, h in zip(t_values, h_values):
    print(f"{t:.3f}    {h:.4f}")

