from ariadne import make_executable_schema

from .schema import compiled_schema
from .resolvers import query, films, categories, actors


schema = make_executable_schema(compiled_schema, query, films, categories, actors)
