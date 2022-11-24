from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLHTTPHandler
from graphql import MiddlewareManager

from .schema import compiled_schema
from .resolvers import query, films, categories, actors, mutation
from .extensions import DatabaseExtension

schema = make_executable_schema(compiled_schema, query, mutation, films, categories, actors)

graphql_app = GraphQL(
    schema,
    http_handler=GraphQLHTTPHandler(
        extensions=[DatabaseExtension]
    ),
)
