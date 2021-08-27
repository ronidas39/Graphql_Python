import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
course_name="computer sience"
course_time_year=1
class course(graphene.ObjectType):
    name= graphene.String()
    duration=graphene.Int()
    def resolve_name(self,info):
        return course_name
    def resolve_duration(self,into):
        return course_time_year
app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=course)))
print(graphene.Schema(query=course))