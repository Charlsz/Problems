import random
import time
import matplotlib.pyplot as plt

# Función para multiplicar dos números de N pares de cifras
def multiply_large_numbers(N):
    num1 = random.randint(10**(N-1), 10**N - 1)
    num2 = random.randint(10**(N-1), 10**N - 1)
    result = num1 * num2
    return result

# Función para calcular la complejidad teórica (O(N^2))
def theoretical_complexity(N):
    return N**2

# Función para calcular la complejidad práctica (medición de tiempo promedio)
def practical_complexity(N, num_samples=1000):
    total_time = 0
    for _ in range(num_samples):
        start_time = time.time()
        multiply_large_numbers(N)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / num_samples
    return average_time

# Crear listas para almacenar los valores de N y las complejidades
N_values = []
theoretical_complexities = []
practical_complexities = []

# Calcular complejidades para diferentes valores de N
for N in range(1, 11):
    N_values.append(N)
    theoretical_complexities.append(theoretical_complexity(N))
    practical_complexities.append(practical_complexity(N))

# Graficar complejidad teórica
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(N_values, theoretical_complexities, label='Complejidad Teórica (O(N^2))')
plt.xlabel('N')
plt.ylabel('Tiempo / Complejidad')
plt.legend()
plt.title('Complejidad Teórica')

# Graficar complejidad práctica
plt.subplot(1, 2, 2)
plt.plot(N_values, practical_complexities, label='Complejidad Práctica Promedio')
plt.xlabel('N')
plt.ylabel('Tiempo (Promedio)')
plt.legend()
plt.title('Complejidad Práctica')

plt.tight_layout()
plt.show()

