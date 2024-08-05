import numpy as np
import matplotlib.pyplot as plt

def psi_n(n, L, x):
    """Função de onda para uma partícula em uma caixa 1D"""
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def classical_prob(x1, x2, L):
    """Probabilidade clássica para duas partículas"""
    return np.ones_like(x1) / L**2  # Distribuição uniforme

def quantum_symmetric(x1, x2, L):
    """Função de onda simétrica (bósons)"""
    psi1 = psi_n(1, L, x1) * psi_n(2, L, x2)
    psi2 = psi_n(2, L, x1) * psi_n(1, L, x2)
    return (psi1 + psi2) / np.sqrt(2)

def quantum_antisymmetric(x1, x2, L):
    """Função de onda antissimétrica (férmions)"""
    psi1 = psi_n(1, L, x1) * psi_n(2, L, x2)
    psi2 = psi_n(2, L, x1) * psi_n(1, L, x2)
    return (psi1 - psi2) / np.sqrt(2)

# Parâmetros
L = 1  # Comprimento da caixa
N = 100  # Número de pontos na grade

# Criar grade de pontos
x1, x2 = np.meshgrid(np.linspace(0, L, N), np.linspace(0, L, N))

# Calcular probabilidades
prob_classical = classical_prob(x1, x2, L)
prob_bosons = np.abs(quantum_symmetric(x1, x2, L)) ** 2
prob_fermions = np.abs(quantum_antisymmetric(x1, x2, L)) ** 2

# Plotar resultados
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Ajustar a visualização da probabilidade clássica
im1 = ax1.imshow(prob_classical, extent=[0, L, 0, L], origin='lower', vmin=0, vmax=prob_classical.max())
ax1.set_title('Clássico')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
fig.colorbar(im1, ax=ax1)

im2 = ax2.imshow(prob_bosons, extent=[0, L, 0, L], origin='lower')
ax2.set_title('Quântico (Bósons)')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
fig.colorbar(im2, ax=ax2)

im3 = ax3.imshow(prob_fermions, extent=[0, L, 0, L], origin='lower')
ax3.set_title('Quântico (Férmions)')
ax3.set_xlabel('x1')
ax3.set_ylabel('x2')
fig.colorbar(im3, ax=ax3)

plt.tight_layout()
plt.show()
