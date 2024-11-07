## Manual de Referencia: Red de Hopfield

Este manual describe la aplicación de consola que implementa una Red de Hopfield. Cubre sus alcances y limitaciones, el proceso de instalación, cómo ejecutar la red y algunas preguntas frecuentes.

### 1. Alcances y Limitaciones:

**Alcances:**

- **Almacenamiento y Recuperación de Patrones:** La aplicación permite entrenar una red de Hopfield con un conjunto de patrones binarios y recuperar patrones a partir de versiones ruidosas o incompletas.
- **Visualización:** Muestra los patrones originales, con ruido y recuperados para una evaluación visual del rendimiento de la red.
- **Configuración Flexible:** Permite configurar el tamaño de la red (20x20, 50x50, 100x100) y seleccionar entre diferentes datasets de patrones.
- **Control de Ruido:** Permite al usuario especificar el nivel de ruido a agregar al patrón de prueba.

**Limitaciones:**

- **Capacidad Limitada:** La red de Hopfield tiene una capacidad de almacenamiento limitada. Almacenar demasiados patrones puede llevar a interferencia y a la incapacidad de recuperar los patrones correctamente.
- **Patrones Similares:** Patrones muy similares pueden causar confusión en la red, dificultando la recuperación del patrón correcto.
- **Mínimos Locales Espurios:** La red puede converger a un patrón solapado, que no corresponde a ningún patrón almacenado.
- **Solo Patrones Binarios:** Esta implementación solo soporta patrones binarios (-1 y 1). No se admiten patrones con valores continuos.

### 2. Proceso de Instalación:

1. **Requisitos:** Asegúrate de tener Python 3 instalado en tu sistema. También necesitas las siguientes bibliotecas: NumPy, Matplotlib. Puedes instalarlas usando pip:

   ```bash
   pip install numpy matplotlib pandas
   ```

2. **Descarga del Código:** Descarga el código fuente de la aplicación.

3. **Datasets:** Asegúrate de tener los archivos `dataset_1.csv`, `dataset_2.csv` y `dataset_3.csv` en el directorio `/datasets`. Estos archivos contienen los datos de entrenamiento para la red.

4. **Ejecución:** Navega al directorio donde se encuentra el código fuente en la terminal y ejecuta el script principal:

   ```bash
   python main.py
   ```

### 3. Ejecutar la red:

1. **Configurar la Red:** Al iniciar la aplicación, selecciona la opción 1 y elige un tamaño para la red (por ejemplo, 100x100).

2. **Entrenar la Red:** Selecciona la opción 2 y elige un dataset (por ejemplo, dataset_1.csv). La red se entrenará con los patrones del dataset seleccionado.

3. **Probar la Red:** Selecciona la opción 3. Elige un patrón del dataset para probar. Ingresa un nivel de ruido (por ejemplo, 0.1). La aplicación mostrará tres imágenes: el patrón original, el patrón con ruido y el patrón recuperado por la red. Observa cómo la red intenta reconstruir el patrón original a partir de la versión ruidosa.

4. **Cambiar configuración:** Si desea cambiar la configuración o el dataset elegido, solo debes dirigirse a las opciones correspondientes del menu y hacer el cambio.

### 4. Preguntas frecuentes:

**P1: ¿Qué significan los valores -1 y 1 en los patrones?**

Representan los dos estados posibles de una neurona en la red de Hopfield. Puedes interpretarlos como "apagado" (-1) y "encendido" (1), o como valores binarios 0 y 1, respectivamente.

**P2: ¿Cómo puedo interpretar los resultados?**

La aplicación mostrará tres imágenes: el patrón original, el patrón con ruido añadido y el patrón recuperado por la red. Cuanto más se parezca el patrón recuperado al original, mejor será el rendimiento de la red.

**P3: ¿Qué significa el nivel de ruido?**

El nivel de ruido es un valor entre 0.0 y 0.5 que representa la proporción de píxeles que se invertirán aleatoriamente en el patrón de prueba. Un nivel de ruido de 0.1 significa que el 10% de los píxeles se modificarán.

**P4: ¿Qué pasa si la red no recupera el patrón correctamente?**

Esto puede deberse a varias razones:

- **Demasiado ruido:** Intenta reducir el nivel de ruido.
- **Capacidad de la red:** Si se han almacenado demasiados patrones, la red puede tener dificultades para recuperarlos. Intenta usar una red más grande o reducir el número de patrones de entrenamiento.
- **Patrones similares:** Si los patrones de entrenamiento son muy similares, la red puede confundirse. Intenta usar patrones más distintos.

### 5. Diagrama de Flujo Simplificado:

![alt text](https://res.cloudinary.com/dces3r2pe/image/upload/v1731019052/ihzbydwlu5flpvozdsb9.png)

### 6. Estructura del Código:

- **`HopfieldNetwork` class:** Contiene la lógica principal de la red de Hopfield: inicialización, entrenamiento y recuperación de patrones.
- **`datasets.py`:** Contiene funciones para cargar los datasets desde los archivos CSV.
- **`plots.py`:** Contiene la función `plot_patterns` para visualizar los patrones.
- **Funciones de Utilidad:** Funciones como `clear_console`, `show_menu`, `get_size`, `select_noise`, `select_dataset` y `select_pattern` gestionan la interacción con el usuario y la configuración de la red.

### 7. Consideraciones Adicionales:

- **Escalabilidad:** Para redes muy grandes, el tiempo de entrenamiento y recuperación puede ser significativo.
