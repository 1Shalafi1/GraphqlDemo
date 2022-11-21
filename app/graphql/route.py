import os

from ariadne import make_executable_schema
from ariadne.wsgi import GraphQL

from app.graphql.resolvers import query, union
from app.graphql.schema import type_defs

ariadne_schema = make_executable_schema(type_defs, [query, union])

# application = GraphQL(ariadne_schema)
