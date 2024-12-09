import numpy as np
import matplotlib.pyplot as plt

# Definimos la función h(t) y su derivada h'(t)
def h(t):
    return 5*t**2 + 10*t + 100

def h_prime(t):
    return 10*t + 10

# Generamos los valores de t
t = np.linspace(-10, 10, 400)

# Calculamos los valores de h(t) y h'(t)
h_values = h(t)
h_prime_values = h_prime(t)

