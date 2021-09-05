import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from mapping import query

app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=query)))
print(graphene.Schema(query=query))