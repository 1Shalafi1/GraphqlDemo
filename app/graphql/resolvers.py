from ariadne import ObjectType, QueryType

from app.database.models.actor import Actor
from app.database.models.category import Category
from app.database.models.film import Film
from app.dependencies.database import DBSession


query = QueryType()

films = ObjectType("Film")
categories = ObjectType("Category")
actors = ObjectType("Actor")


@query.field("actors")
@films.field("actors")
def resolve_actors(obj, info, limit: int = 10, skip: int = 0):
    with DBSession() as db:
        if obj:
            actor_objects = obj.actors
        else:
            actor_objects = Actor.get_filtered(db=db, limit=limit, skip=skip)
    return actor_objects


@query.field("categories")
@films.field("categories")
def resolve_categories(obj, info, limit: int = 10, skip: int = 0):
    with DBSession() as db:
        if obj:
            category_objects = obj.categories
        else:
            category_objects = Category.get_filtered(db=db, limit=limit, skip=skip)
    return category_objects


@query.field("films")
@actors.field("films")
def resolve_films(obj, info, limit: int = 10, skip: int = 0):
    with DBSession() as db:
        if obj:
            film_objects = obj.films
        else:
            film_objects = Film.get_filtered(db=db, limit=limit, skip=skip)
    return film_objects

