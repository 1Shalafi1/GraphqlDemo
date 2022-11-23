from ariadne import make_executable_schema

from .schema import compiled_schema
from .resolvers.actor import queries as ActorQueries
from .resolvers.film import queries as FilmQueries, films

schema = make_executable_schema(compiled_schema, films, ActorQueries, FilmQueries)
