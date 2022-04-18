<h1 align="center">FerBar Market 🛒</h1>

> Este es un marketplace hecho con el microframework de Python "Flask". [Booking.com](https://booking.com/). <br>
![scraper_main](https://user-images.githubusercontent.com/90936639/154614011-c5a6be0a-7e74-4fce-b743-9d6cea865504.png)

>  El repositorio consta de:
> - El script [run.py](run.py) que contiene el módulo que corre la aplicación.
> - La carpeta [models](/models) que contiene los modelos de nuestra aplicación.
> - El script [booking_filtration.py](booking_filtration.py) que filtra las habitaciones por su puntuación en estrellas y el precio más bajo disponible.
> - El script [run.py](run.py) que ejecuta el bot y sus acciones en base a los requerimientos del usuario.
> - Un archivo [constants.py](constants.py) que contiene las variables constantes como la URL del sitio.

## Pre-Requisitos
- Tener Python instalado con una versión superior a la 3.8.


## Como Usarlo
1. Ve al directorio donde quieras crear el proyecto y clona el repositorio

    ```
    git clone https://github.com/Fer-Bar/FerBar-Market.git
    ```
2. Crea un entorno virtual:
    ```
    python3 -m venv venv
    ```
    Una vez creado puedes activarlo.
    <br>

    En Windows ejecutando:
    ```
    venv\Scripts\activate.bat
    ```
    En Unix o MacOS, ejecutando:
    ```
    source venv/bin/activate
    ```
3. Instala las depedencias `pip install -r requirements.txt`
4. Crear un archivo `.env` que contenga las variables de entorno, en especial debe tener una constante llamada SECRET_KEY que contenga un valor secreto.<br>
 - El archivo `.env` debera verse así (Este es un ejemplo de como aplicar la variable de entorno, si quiere puede cambiar los valores):

    ```
    SECRET_KEY=d4s1>Vx@OI+Fqc*}WRy$9u>Akpp|u=V@zwRc{An?up8(x5LV.aq'[~:a%hnt4kZ
    ```

5. Ir a la consola y ejecutar la consola virtual de python.

    ```
    $ python
    ```
  - Luego ejecutar el comando para crear los modelos o tablas:

    ```
    >>> from market import db
    >>> db.create_all()
    ```

6. Ejecutar [run.py](run.py), se puede editar el archivo run.py para cambiar el puerto donde se correra la app.
