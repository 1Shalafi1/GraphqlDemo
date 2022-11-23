from ariadne import ObjectType

from app.database.models.actor import Actor
from app.dependencies.database import DBSession

queries = ObjectType("Query")


@queries.field("actors")
def resolve_actors(obj, context, limit: int = 10, skip: int = 0):
    with DBSession() as db:
        actors = Actor.get_list(db=db, limit=limit, skip=skip)
    return actors
