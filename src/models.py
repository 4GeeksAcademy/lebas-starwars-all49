from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="user")


class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="planet")


class People(db.Model):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(
        Text, nullable=False)

    favorites: Mapped[list["Favorite"]] = relationship(back_populates="people")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


class Favorite(db.Model):
    __tablename__ = "favorite"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(
        ForeignKey("planet.id"), nullable=True)
    people_id: Mapped[int] = mapped_column(
        ForeignKey("people.id"), nullable=True)

    user: Mapped["User"] = relationship(back_populates="favorites")
    planet: Mapped["Planet"] = relationship(back_populates="favorites")
    people: Mapped["People"] = relationship(back_populates="favorites")


"""



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
