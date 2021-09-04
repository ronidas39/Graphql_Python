import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

class player(graphene.Interface):
    name=graphene.String()
    country=graphene.String()

class footballplayer(graphene.ObjectType):
    class Meta:
        interfaces=(player,)
    position=graphene.String()

class cricketplayer(graphene.ObjectType):
    class Meta:
        interfaces=(player,)
    battingorder=graphene.Int()

class query(graphene.ObjectType):
    class Meta:
        name="interfacequery"
        description="implements field type from interface"
    fplayer=graphene.Field(footballplayer,description="coming from football player interface")
    def resolve_fplayer(self,info):
        return {"name":"player1","country":"Spain","position":"Central Back"}
    cplayer=graphene.Field(cricketplayer,description="coming from cricket player interface")
    def resolve_cplayer(self,info):
        return {"name":"player2","country":"India","battingorder":1}

app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=query)))
print(graphene.Schema(query=query))
