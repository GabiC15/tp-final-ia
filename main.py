import numpy as np
from datasets import get_dataset
from plots import plot_patterns
from time import sleep
import os

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        for pattern in patterns:
            pattern = pattern.reshape(self.size)
            self.weights += np.outer(pattern, pattern)
        np.fill_diagonal(self.weights, 0)

    def recall(self, pattern, steps=10):
        pattern = pattern.reshape(self.size)
        for _ in range(steps):
            for i in range(self.size):
                pattern[i] = np.sign(np.dot(self.weights[i], pattern))
        return pattern

    def add_noise(self, pattern, noise_level=0.1):
        # Agrega ruido al patrón
        noisy_pattern = pattern.copy()
        num_noisy = int(noise_level * self.size)
        noise_indices = np.random.choice(range(self.size), num_noisy, replace=False)
        noisy_pattern[noise_indices] *= -1
        return noisy_pattern
    
    def clean_train(self):
        self.weights = np.zeros((size, size))



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu(size, dataset):
    print("\033[94m****************************************\033[0m")
    print("\033[94m*           Red de Hopfield            *\033[0m")
    print("\033[94m****************************************\033[0m")
    if size: 
      wh = f'{int(np.sqrt(size))} * {int(np.sqrt(size))}'
      print(f"\nTamaño: \033[92m{wh}\033[0m")
    if dataset: print(f"Dataset: \033[92m{dataset}\033[0m")
    print("\n\033[92m1.\033[0m Configurar Red")
    print("\033[92m2.\033[0m Entrenar Red")
    print("\033[92m3.\033[0m Probar Red")
    print("\033[92m4.\033[0m Salir")


def get_size():
    while True:
        try:
            size_option = int(input("\n\033[93mSeleccione el tamaño de la red:\033[0m\n\033[92m1.\033[0m 20x20 \n\033[92m2.\033[0m 50x50 \n\033[92m3.\033[0m 100x100 \n\033[95m-> \033[0m"))
            if 1 <= size_option <= 3:
                sizes = {1: 20 * 20, 2: 50 * 50, 3: 100 * 100}
                return sizes[size_option]
            else:
                print("\033[91mOpción inválida. Intente de nuevo.\033[0m")
                sleep(1)
        except ValueError:
            print("\033[91mEntrada inválida. Ingrese un número.\033[0m")
            sleep(1)


def select_noise():
    while True:
        try:
            noise_level = float(input("\n\033[93mIngrese el nivel de ruido (0.0 - 0.5):\033[0m \n\033[95m-> \033[0m"))
            if 0 <= noise_level <= 0.5:
                return noise_level
            else:
                print("\033[91mEl nivel de ruido debe estar entre 0.0 y 0.5. Intente de nuevo.\033[0m")
                sleep(1)
        except ValueError:
            print("\033[91mEntrada inválida. Ingrese un número.\033[0m")
            sleep(1)

        
def select_dataset(size):
    while True:
        try:
            dataset_option = int(input("\n\033[93mSeleccione el dataset:\033[0m\n\033[92m1.\033[0m dataset_1.csv (Iconos) \n\033[92m2.\033[0m dataset_2.csv (Letras) \n\033[92m3.\033[0m dataset_3.csv (Rostros) \n\033[95m-> \033[0m"))
            filenames = ['dataset_1.csv', 'dataset_2.csv', 'dataset_3.csv']
            if 1 <= dataset_option <= len(filenames):
                filename = filenames[dataset_option - 1]
                training_data = get_dataset(filename=filename, size=size)
                return training_data, filename

            else:
                print("\033[91mOpción de dataset inválida. Intente de nuevo.\033[0m")
                sleep(1)

        except ValueError:
            print("\033[91mEntrada inválida. Ingrese un número.\033[0m")
            sleep(1)
        except FileNotFoundError:
            print(f"\033[91mError: Archivo {filename} no encontrado.\033[0m")
            sleep(1)
            return None, filename

def select_pattern():
    while True:
        try:
          pattern_index = int(input(f"\n\033[93mSeleccione el patrón (1-{len(training_data)}):\033[0m \n\033[95m-> \033[0m"))
          if 1 <= pattern_index < len(training_data) + 1:
              return pattern_index - 1
          else:
              print("\033[91mÍndice de patrón inválido. Intente de nuevo.\033[0m")
              sleep(1)
                    

        except ValueError:
            print("\033[91mEntrada inválida. Ingrese un número.\033[0m")
            sleep(1)


if __name__ == "__main__":

    network = None
    training_data = None
    selected_file = None
    size = None

    while True:
        clear_console()
        show_menu(size=size, dataset=selected_file)

        try:
            option = int(input("\n\033[95mIngrese una opción: \033[0m"))

            if option == 1:
                size = get_size()
                network = HopfieldNetwork(size)
                print("\033[92mRed configurada correctamente.\033[0m")
                sleep(1)

            elif option == 2:
                if network is None:
                    print("\033[91mPrimero configure la red (opción 1).\033[0m")
                    sleep(1)
                    continue

                training_data, selected_file = select_dataset(network.size)

                if training_data is not None:
                    network.clean_train()
                    network.train(training_data)
                    print("\033[92mRed entrenada correctamente.\033[0m")
                    sleep(1)



            elif option == 3:
                data_size = len(training_data[0])
                if network is None or training_data is None:
                    print("\033[91mPrimero configure y entrene la red (opciones 1 y 2).\033[0m")
                    sleep(1)
                    continue
                elif data_size != network.size:
                    print("\033[91mDebe reentrenar la red (opción 2).\033[0m")
                    sleep(1)
                    continue
                
                pattern_index = select_pattern()
                if training_data is not None:
                    test_pattern = training_data[pattern_index]
                    noise_level = select_noise()
                    noisy_pattern = network.add_noise(test_pattern.copy(), noise_level=noise_level)  # Agregar .copy()
                    recalled_pattern = network.recall(noisy_pattern.copy())
                    plot_patterns(test_pattern, noisy_pattern, recalled_pattern, size=network.size)


            elif option == 4:
                print("\033[94mSaliendo...\033[0m")
                break
            else:
                print("\033[91mOpción inválida. Intente de nuevo.\033[0m")
                sleep(1)

        except ValueError:
            print("\033[91mEntrada inválida. Ingrese un número.\033[0m")
            sleep(1)