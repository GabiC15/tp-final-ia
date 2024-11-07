from math import sqrt

# Visualización (opcional) del patrón original, ruidoso y recordado
import matplotlib.pyplot as plt
def plot_patterns(original, noisy, recalled, size = 100*100):
    length = int(sqrt(size))
    # Configuramos una figura con 1 fila y 3 columnas para los tres patrones
    fig, axes = plt.subplots(1, 3, figsize=(10, 4))

    # Mostrar el patrón original
    axes[0].imshow(original.reshape(length, length), cmap='binary')
    axes[0].set_title("Patrón Original")
    axes[0].axis('off')

    # Mostrar el patrón con ruido
    axes[1].imshow(noisy.reshape(length, length), cmap='binary')
    axes[1].set_title("Patrón con Ruido")
    axes[1].axis('off')

    # Mostrar el patrón recordado
    axes[2].imshow(recalled.reshape(length, length), cmap='binary')
    axes[2].set_title("Patrón Recordado")
    axes[2].axis('off')

    # Mostrar todos los patrones en una sola ventana
    plt.show()