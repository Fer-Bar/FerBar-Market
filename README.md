<h1 align="center">FerBar Market 🛒</h1>

> Este es un marketplace hecho con el microframework de Python "Flask" y desplegado en Heroku. [Let's see my website](https://ferbarmarket.herokuapp.com/). <br>
> 
![ferbar-logo](https://user-images.githubusercontent.com/90936639/163207495-57e6c611-dfb9-410e-a7cf-f31ecd08fa61.png)

>  El repositorio consta de:
> - La carpeta [models](/models) que contiene los modelos de nuestra aplicación: user.py y item.py.
> - El módulo [forms.py](forms.py) que contiene los formularios de la aplicación.
> - El módulo __[init__.py](__init__.py) que contiene la configuración de nuestra aplicación y la creación de la misma. Hace más sencillo trabajar con las importaciones.
> - Un módulo [routes.py](routes.py) que contiene las rutas de nuestra aplicación, se utiliza para asignar una URL específica con una función asociada a esta, la misma esta destinada a realizar una determinada tarea.
> - El módulo [run.py](run.py) que contiene el módulo que corre la aplicación.

## 💻 Pre-Requisitos
- Tener Python instalado con una versión superior a la 3.8.
- Tener instalado Docker o Docker Desktop


## ⚙️ Cómo Usarlo
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
 - El archivo `.env` debera verse así (Este es un ejemplo de como aplicar la variable de entorno):

    ```
    SECRET_KEY=d4s1>Vx@OI+Fqc*}WRy$9u>Akpp|u=V@zwRc{An?up8(x5LV.aq'[~:a%hnt4kZ
    ``` 

5. Ir a la consola interactiva de python y ejecutar el comando "python" en el root del proyecto. 

    ```
    C:\Users\HP\Documents\ferbarmarket 
    $ python
    ```     
  - Luego ejecutar el siguiente comando para crear los modelos o tablas:

    ```
    >>> from market import db
    >>> db.create_all()
    ``` 

6. Ejecutar [run.py](run.py), se puede editar el archivo run.py para cambiar el puerto donde se correra la app.

7. Dockerizando la aplicación... en breve se actualizara el readme.md con las nuevas configuraciones.
