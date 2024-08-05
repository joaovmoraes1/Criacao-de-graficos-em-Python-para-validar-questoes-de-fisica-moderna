import numpy as np
import matplotlib.pyplot as plt

def density_of_states(E, V, m):
  """Densidade de estados para um gás de Fermi 3D."""
  return (V / (2 * np.pi**2)) * ((2 * m / (hbar**2))**(3/2)) * np.sqrt(E)

def fermi_energy(n, V, m):
  """Cálculo da energia de Fermi."""
  return (hbar**2 / (2 * m)) * (3 * np.pi**2 * n / V)**(2/3)

def total_energy(EF, V, m):
  """Cálculo da energia total integrando a densidade de estados."""
  return (3/5) * EF * V * density_of_states(EF, V, m)

# Constantes
hbar = 1.0545718e-34  # Constante de Planck reduzida (J.s)
m = 9.1093837e-31  # Massa do elétron (kg)
V = 1e-6  # Volume (m^3)
n = 1e28  # Densidade de partículas (m^-3)

# Cálculo da energia de Fermi
EF = fermi_energy(n, V, m)

# Cálculo da energia total
E_total = total_energy(EF, V, m)

print(f"Energia de Fermi: {EF:.2e} J")
print(f"Energia Total: {E_total:.2e} J")

# Plotagem da densidade de estados
E = np.linspace(0, 2*EF, 1000)
DOS = density_of_states(E, V, m)


plt.figure(figsize=(10, 6))
plt.plot(E, DOS)
plt.fill_between(E, DOS, where=(E <= EF), alpha=0.3)
plt.axvline(x=EF, color='r', linestyle='--', label='Energia de Fermi')
plt.xlabel('Energia (J)')
plt.ylabel('Densidade de Estados')
plt.title('Densidade de Estados para um Gás de Fermi 3D')
plt.legend()
plt.grid(True)
plt.show()