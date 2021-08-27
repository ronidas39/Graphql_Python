import graphene
from fastapi import FastAPI
from graphene.types.objecttype import ObjectType
from starlette.graphql import GraphQLApp
from graphene import ObjectType as ot
from graphene import String as st
from graphene import Int as int
from graphene import List as li

data=[
    {
        "name": "Roni",
        "city": "Cologne",
        "country": "India"

},
{
        "name": "John",
        "city": "London",
        "country": "UK"

},
{
         "name": "Maria",
         "city": "Sydney",
         "country": "Australia"
}
]

class students(ot):
    name=st()
    city=st()
    country=st()

class person(ot):
    student=li(students)
    def resolve_student(self,info):
        return data
app=FastAPI()
app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(query=person)))
print(graphene.Schema(query=person))
