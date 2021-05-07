# Semana Tec: El arte de la programación (2021)

Equipo 2:
- Ana María Lugo Gama
- Rodrigo Sahagún Lomelí Cárdenas
- Joaquín Gerardo Zenteno García
- Ivana Renee Carmona Limón
- Andrés Alexander Mendoza Equihua
- Ana Cristina Munguía Romero

## Acerca de
Este es un proyecto académico desarrollado durante la semana tec "El arte de la programación" de mayo 2021. El proyecto trata sobre el procesamiento de imágenes, por lo cual se desarrolló un código con 6 filtros diferentes, que puedes correr desde tu computadora. A continuación se presentarán algunos prerequisitos para poder correr el programa, y el uso con su explicación. 

## Instalar dependencias
- Open CV
- Python 3

## Uso
Clonar repositorio y pegar el link en la terminal: ```git clone https://github.com/Rodrigo-bit45/semanatec.git```

El siguiente paso es escribir el parámetro ```-cam``` que se muestra a continuación para escoger qué cámara usar (default es 0)

```python3 camera_python.py -cam 0```

Una vez escogiendo la cámara deseada, se usará el parámetro ```-menu``` para así escoger uno de los 5 filtros disponibles (default es 0)

```python3 camera_python.py -menu 4```

Cabe recalcar que para usar uno de los 6 filtros disponibles, debes seleccionar un número entre el 0 y el 5, si no escribes un número de ese rango, el programa te pedirá escribir de nuevo un número válido:
- Filtro 0: Borroso
- Filtro 1: Blanco y Negro 
- Filtro 2: Sepia
- Filtro 3: Cartoon
- Filtro 4: Sharpen 
- Filtro 5: Green color detection 

## REFERENCIAS
- Krunal. (2020). How to convert RGB image to Grayscale in Python. AppDividend. Recuperado de: https://appdividend.com/2020/06/17/how-to-convert-rgb-image-to-grayscale-in-python/
- Borcan, M. (2020). Python OpenCV: Building Instagram-Like Image Filters. Towards Data Science. Recuperado de: https://towardsdatascience.com/python-opencv-building-instagram-like-image-filters-5c482c1c5079
- Ebrahim, M. (2020). Tutorial de procesar imágenes en Python (usando OpenCV). LIKE geeks. Recuperado de: https://likegeeks.com/es/procesar-de-imagenes-en-python/
- How to apply filters to images using Python and OpenCV (2020). Recuperado de: https://image4.io/en/blog/how-to-apply-filters-to-images-using-python-and-opencv/
- Converting An Image To A Cartoon Using OpenCV (2020) OIM. Recuperado de: https://analyticsindiamag.com/converting-an-image-to-a-cartoon/
