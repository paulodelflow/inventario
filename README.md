# Django Product Dashboard

Este es un proyecto de Django que muestra una lista de productos con la funcionalidad para ordenar y visualizar detalles como la cantidad de productos, clientes, ingresos y más. También permite cargar imágenes para los productos.

## Características

- Listado de productos con imágenes, cantidades, clientes y ganancias.
- Funcionalidad de ordenación para visualizar productos según diferentes criterios.
- Carga de imágenes para productos.
- Diseño responsivo y moderno.

## Requisitos

- Python 3.x
- Django 5.0.6
- Pillow (para manejo de imágenes)
- Ruby (para Compass)
- Node.js (para Angular)

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/paulodelflow/inventario
    cd inventario
    ```

2. **Crear y activar un entorno virtual:**

    ```bash
    python -m venv .env
    source .env/bin/activate  # En Windows usa `.env\Scripts\activate`
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar la base de datos:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Crear un superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Cargar datos iniciales (si tienes fixtures o datos de ejemplo):**

    ```bash
    python manage.py loaddata initial_data.json  # Si tienes un archivo de datos iniciales
    ```

## Ejecución del Servidor

1. **Ejecutar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

2. **Abrir tu navegador y visitar:**

    ```text
    http://127.0.0.1:8000/
    ```

## Archivos Estáticos

Para servir archivos estáticos (CSS, JavaScript, imágenes), asegúrate de haber configurado correctamente `STATIC_URL` y `STATICFILES_DIRS` en tu archivo `settings.py`.

## Estructura del Proyecto

- **dash**: Contiene los modelos, vistas y plantillas para la funcionalidad principal.
- **static**: Archivos CSS, JavaScript y otros archivos estáticos.
- **templates**: Archivos HTML.
- **media**: Carpeta donde se almacenarán las imágenes cargadas de los productos.

## Contribuir

1. **Fork el repositorio**
2. **Crea una nueva rama para tu funcionalidad o corrección de errores:**

    ```bash
    git checkout -b feature/nueva-funcionalidad
    ```

3. **Realiza tus cambios y commitea:**

    ```bash
    git commit -m "Agrega nueva funcionalidad"
    ```

4. **Envía tus cambios a tu fork:**

    ```bash
    git push origin feature/nueva-funcionalidad
    ```

5. **Crea un Pull Request**

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para cualquier pregunta o comentario, por favor contacta a [pa.escobarrm@duocuc.cl](mailto:pa.escobarrm@duocuc.cl).
