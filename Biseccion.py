def f(t):
    h0 = 0
    v0 = 30
    g = 9.81
    return h0 + v0 * t - 0.5 * g * t**2 - 150

def bisection_method(a, b, tol=1e-4):
    if f(a) * f(b) > 0:
        print("No hay raíz en el intervalo inicial")
        return None

    iterations = []
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        iterations.append((a, b, c, f(a), f(b), fc))
        if fc == 0:
            break
        elif f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2, iterations

# Definir intervalo inicial
a = 0
b = 10  # Seleccionamos un valor suficientemente grande

# Aplicar el método de bisección
root, iteraciones = bisection_method(a, b)

# Mostrar resultados
print(f"La raíz se encuentra en t = {root:.4f}")

# Mostrar tabla de iteraciones
print("\nIteraciones:")
print("Iteración | a        | b        | c        | f(a)      | f(b)      | f(c)")
for i, (a, b, c, fa, fb, fc) in enumerate(iteraciones):
    print(f"{i+1:9} | {a:.4f} | {b:.4f} | {c:.4f} | {fa:.4f} | {fb:.4f} | {fc:.4f}")