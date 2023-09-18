import math

def calculate_score(N, objectives):
    dp = [[math.inf] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(i, N + 1):
            for k in range(i - 1, j):
                x1, y1, p1 = objectives[k]
                x2, y2, p2 = objectives[j - 1]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                dp[j][i] = min(dp[j][i], dp[k][i - 1] + distance + p2)

    return dp[N][N]

while True:
    N = int(input("Ingrese el número de objetivos (o 0 para salir): "))
    if N == 0:
        break

    print("Ingrese los objetivos en formato X Y P:")
    objectives = []
    for _ in range(N):
        X, Y, P = map(int, input().split())
        objectives.append((X, Y, P))

    score = calculate_score(N, objectives)
    print(f"La puntuación más baja es: {score:.3f}\n")
