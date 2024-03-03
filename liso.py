import numpy as np
import matplotlib.pyplot as plt

def campo_disco_infinito(x, y, z, sigma):
  """
  Calcula el campo gravitatorio de un disco infinito con distribución de masa proporcional al radio.

  Parámetros:
    x: Coordenada x del punto de observación.
    y: Coordenada y del punto de observación.
    z: Coordenada z del punto de observación (debe ser 0 para un disco infinito).
    sigma: Densidad superficial de masa del disco.

  Retorno:
    Un vector numpy que contiene las componentes x, y, z del campo gravitatorio.
  """

  # Constante gravitatoria universal
  G = 6.67430e-11 # m^3 kg^-1 s^-2

  # Validar la coordenada z
  if z != 0:
    raise ValueError("La coordenada z debe ser 0 para un disco infinito.")

  # Cálculo del campo gravitatorio en el plano z = 0
  campo_xy = np.zeros((2,))
  for r in np.linspace(0, np.inf, 1000):
    campo_xy += G * sigma * r / (x**2 + y**2 + r**2)**(1.5) * np.array([x, y])

  # Retorno del campo gravitatorio
  return np.array([campo_xy[0], campo_xy[1], 0])

# Ejemplo de uso
x = 1 # m
y = 2 # m
z = 0 # m
sigma = 1e3 # kg/m^2

campo = campo_disco_infinito(x, y, z, sigma)

print(f"Campo gravitatorio en ({x}, {y}, {z}):")
print(f"  x: {campo[0]} m/s^2")
print(f"  y: {campo[1]} m/s^2")
print(f"  z: {campo[2]} m/s^2")


# Constantes
G = 6.67430e-11 # m^3 kg^-1 s^-2
sigma = 1.17e10 # kg/m^2

