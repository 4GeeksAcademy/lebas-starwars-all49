from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)


    



"""
📝 Instrucciones

Table user: 
    id: int
    lastname: str
    email: str
    password: str

Table planet:
    id: int
    name: str
    description: str

Table people:
    id: int
    name: str
    description: str

    
asociación 
Table favorite:
    id: int
    user_id: int
    planet_id: int     id ---  user_id ----- people_id ---- planet_id ----
    people_id: int      1         1             1              null
                        2         1             null             1       


Crea una API conectada a una base de datos e implemente los siguientes endpoints (muy similares a SWAPI.dev or SWAPI.tech):

    [GET] /people Listar todos los registros de people en la base de datos.
    [GET] /people/<int:people_id> Muestra la información de un solo personaje según su id.
    [GET] /planets Listar todos los registros de planets en la base de datos.
    [GET] /planets/<int:planet_id> Muestra la información de un solo planeta según su id.

Adicionalmente, necesitamos crear los siguientes endpoints para que podamos tener usuarios y favoritos en nuestro blog:

    [GET] /users Listar todos los usuarios del blog.
    [GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
    [POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el id = planet_id.
    [POST] /favorite/people/<int:people_id> Añade un nuevo people favorito al usuario actual con el id = people_id.
    [DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id.
    [DELETE] /favorite/people/<int:people_id> Elimina un people favorito con el id = people_id.
    [GET] /people-population Popula la tabla de base de datos de people --> Consultar apis desde el backend

    Tu API actual no tiene un sistema de autenticación (todavía), es por eso que la única forma de crear usuarios es directamente en la base de datos usando el Flask admin.



    - Alvaro - Tabla user 
    - Antonio - Tabla Planet
    - Eric - Tabla people
    - Guillermo - Tabla de favorite
    - Javiera - Realations
    - Jose David - get people
    - Julian - pepple por id
    - Maria - get planets
    - Tobias - get plants is
    - Valentina - añadir un planeta a favorite

"""
