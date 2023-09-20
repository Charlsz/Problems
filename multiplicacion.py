import random
import time
import matplotlib.pyplot as plt

def karatsuba(x, y):
    # Si los números son de un solo dígito, realiza una multiplicación simple
    timea = time.time()
    if x < 10 or y < 10:
        return x * y

    # Calcula el número de dígitos de los números
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    # Divide los números en partes más pequeñas
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)

    # Calcula los productos intermedios recursivamente
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # Calcula el resultado final
    result = ac * 10**(2 * n2) + ad_bc * 10**n2 + bd
    timeb = time.time()
    print(f"Tiempoo en la funcion: {timeb-timea}")
    return result

# Listas para almacenar los tamaños de entrada (n) y los tiempos de ejecución
input_sizes = []
execution_times = []

# Generar números aleatorios y medir el tiempo de ejecución para diferentes tamaños de entrada
for n in range(1, 7):
    num1 = random.randint(10**(n-1), 10**n - 1)
    num2 = random.randint(10**(n-1), 10**n - 1)
    start_time = time.time()
    resultado = karatsuba(num1, num2)
    end_time = time.time()
    elapsed_time = (end_time - start_time)
    input_sizes.append(n)
    execution_times.append(elapsed_time)
    print(f"Tamaño de entrada n={n}: Tiempo de ejecución = {elapsed_time:.15f} segundos")

# Crear una gráfica de complejidad práctica
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', label='Tiempo de Ejecución Práctico')
plt.xlabel('Tamaño de Entrada (n)')
plt.ylabel('Tiempo de Ejecución (segundos)')

# Generar la gráfica de complejidad teórica O(n^1.585)
theoretical_complexity = [n ** 1.585 for n in input_sizes]
plt.plot(input_sizes, theoretical_complexity, linestyle='--', label='Complejidad Teórica O(n^1.585)')

plt.legend()
plt.title('Complejidad Práctica vs. Complejidad Teórica')
plt.grid(True)
plt.show()
