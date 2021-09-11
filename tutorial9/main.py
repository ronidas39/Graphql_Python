from schema import cricketplayer, footballplayer, invalid
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from mapping import query

app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=query,types=[footballplayer,cricketplayer,invalid])))
print(graphene.Schema(query=query))
