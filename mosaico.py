import matplotlib.pyplot as plt

MOD = 10**6

def count_tile_patterns(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(M + 1):
        dp[0][j] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[N][M]

def plot_tile_pattern(N, M):
    num_patterns = count_tile_patterns(N, M)

    # Crear una matriz de 1s para representar las baldosas
    tiles = [[1] * M for _ in range(N)]

    # Crear una figura y un eje
    fig, ax = plt.subplots()

    # Dibujar las baldosas
    ax.matshow(tiles, cmap='Blues')

    # Configurar el título
    ax.set_title(f'Patrón de baldosas ({N}x{M}) - {num_patterns} formas únicas')

    # Mostrar la figura
    plt.show()

# Leer las dimensiones de la tira hasta que se ingresen 0 0
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    # Imprimir el resultado numérico
    print(count_tile_patterns(N, M))

    # Crear y mostrar la representación gráfica
    plot_tile_pattern(N, M)
