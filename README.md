# Credit Manager Platform

 App de test proceso de seleccion CMP.


## Getting Started

### Dependencies

* El proyecto esta corriendo con framework python Django y Django rest framework. Utiliza una base de datos sqlite, la cual viene adjunta al codigo para facilitar el levantamiento y evitar ejecucion de migraciones.

### Installing

* DOCKER / DOCKER COMPOSE

### Executing program

```
docker-compose up -d --build
```
* Una vez levantado el proyecto, se debe generar una API-KEY, via Django Commands.
* Se debe ingresar al contenedor de la aplicacion y ejecutar:

```
python3 manage.py create_api_key
```
* Este comando entregara una api key, que debe guardarse en un archivo .env, en la raiz del proyecto, bajo la key API_KEY.

## Swagger

* Se implemento un api doc Swagger, bajo la ruta /swagger...para realizar request autenticadas, se debe presionar el boton de login, e ingresar el Api-Key generado
de la forma "Api-Key [token]". Una vez realizado se pueden probar los endpoint desde la misma interfaz Swagger.


## Authors

 Sebastian Muñoz