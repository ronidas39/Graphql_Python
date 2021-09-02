import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

class myquery(graphene.ObjectType):
    class Meta:
        name="typefrommetaclass1"
        description="description from metaclass1"
    hello=graphene.String(description="hello string")
    bye=graphene.String(description="bye string")
    def resolve_hello(self,info):
        
        return "hello world!!!"
    def resolve_bye(self,info):
        return "good bye!!"
app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=myquery)))
print(graphene.Schema(query=myquery))