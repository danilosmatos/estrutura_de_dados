import matplotlib.pyplot as plt
import numpy as np
import math

# Valores de n
n = np.arange(1, 11)  # de 1 até 10

# Funções de complexidade
O_1 = [1 for _ in n]
O_log_n = [math.log2(x) for x in n]
O_n = [x for x in n]
O_n_log_n = [x * math.log2(x) for x in n]
O_n2 = [x**2 for x in n]
O_2n = [2**x for x in n]
O_nf = [math.factorial(x) for x in n]

# Plotando
plt.figure(figsize=(12, 8))

plt.plot(n, O_1, label="O(1)")
plt.plot(n, O_log_n, label="O(log n)")
plt.plot(n, O_n, label="O(n)")
plt.plot(n, O_n_log_n, label="O(n log n)")
plt.plot(n, O_n2, label="O(n²)")
plt.plot(n, O_2n, label="O(2ⁿ)")
plt.plot(n, O_nf, label="O(n!)")

# Configurações do gráfico
plt.yscale("log")  # Escala logarítmica para visualizar melhor as curvas
plt.xlabel("Tamanho da entrada (n)")
plt.ylabel("Operações (escala log)")
plt.title("Crescimento das Funções de Complexidade")
plt.legend()
plt.grid(True)

plt.show()
