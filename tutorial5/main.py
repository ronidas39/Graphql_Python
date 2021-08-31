from fastapi import FastAPI
import graphene
from graphene.types import schema
from starlette.graphql import GraphQLApp
from mapping import query

app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=query)))
print(graphene.Schema(query=query))
