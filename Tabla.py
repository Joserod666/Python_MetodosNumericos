import numpy as np
import matplotlib.pyplot as plt

# Definimos la función h(t) y su derivada h'(t)
def h(t):
    return 5*t**2 + 10*t + 100  # Ejemplo de función cuadrática

def h_prime(t):
    return 10*t + 10  # Derivada de la función

# Método de Newton-Raphson
def newton_raphson(t0, tol, max_iter):
    t = t0
    iteraciones = []
    
    for i in range(max_iter):
        h_t = h(t)
        h_prime_t = h_prime(t)
        t_next = t - (h_t - 150) / h_prime_t
        
        iteraciones.append((i, t, h_t, h_prime_t, t_next))
        
        if abs(t_next - t) < tol:
            break
        
        t = t_next
    
    return iteraciones

# Parámetros iniciales
t0 = 1.0  # Estimación inicial
tol = 1e-4  # Tolerancia
max_iter = 20  # Número máximo de iteraciones

# Ejecutamos el método de Newton-Raphson
iteraciones = newton_raphson(t0, tol, max_iter)

# Imprimimos la tabla de iteraciones
print(f"{'Iteración':<10}{'t_n':<10}{'h(t_n)':<15}{'h\'(t_n)':<15}{'t_{n+1}':<10}")
for it in iteraciones:
    print(f"{it[0]:<10}{it[1]:<10.4f}{it[2]:<15.4f}{it[3]:<15.4f}{it[4]:<10.4f}")

# Resultado final
t_final = iteraciones[-1][4]
print(f"\nEl tiempo cuando el dron alcanza una altura de 150 metros es aproximadamente t = {t_final:.4f} segundos.")


