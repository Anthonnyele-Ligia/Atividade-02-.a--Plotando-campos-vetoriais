import matplotlib.pyplot as plt
import numpy as np

# Geração de Pontos no R²

x = np.linspace(-10, 10, 10)
y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)


# Campo Vetorial F(x, y) = (y, sin(x))

P = Y                 
Q = np.sin(X)         


# Plotagem do Gráfico

plt.title('Campo Vetorial F(x, y) = <y, sin(x)>')
plt.quiver(X, Y, P, Q, color='Green')
plt.xlabel(' eixo x')
plt.ylabel(' eixo y')
plt.axis('equal')
plt.grid(True)
plt.show()