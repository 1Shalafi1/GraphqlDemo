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
    db = info.context['database_session']
    if obj:
        actor_objects = obj.actors.offset(skip).limit(limit).all()
    else:
        actor_objects = Actor.get_filtered(db=db, limit=limit, skip=skip)
    return actor_objects


@query.field("categories")
@films.field("categories")
def resolve_categories(obj, info, limit: int = 10, skip: int = 0):
    db = info.context['database_session']
    if obj:
        category_objects = obj.categories.offset(skip).limit(limit).all()
    else:
        category_objects = Category.get_filtered(db=db, limit=limit, skip=skip)
    return category_objects


@query.field("films")
@actors.field("films")
@categories.field("films")
def resolve_films(obj, info, limit: int = 10, skip: int = 0):
    db = info.context['database_session']
    if obj:
        film_objects = obj.films.offset(skip).limit(limit).all()
    else:
        film_objects = Film.get_filtered(db=db, limit=limit, skip=skip)
    return film_objects

