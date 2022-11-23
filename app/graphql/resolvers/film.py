from ariadne import ObjectType

from app.database.models.film import Film
from app.dependencies.database import DBSession

queries = ObjectType("Query")
films = ObjectType("Actor")


@films.field("films")
@queries.field("films")
def resolve_films(obj, context, limit: int = 10, skip: int = 0, actor_id=None):
    with DBSession() as db:
        actors = Film.get_list(db=db, limit=limit, skip=skip)
    return actors
