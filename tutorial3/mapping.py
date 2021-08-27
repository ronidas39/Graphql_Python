import graphene
from schema import courses
from data import read_data

class query(graphene.ObjectType):
    course=graphene.List(courses)
    def resolve_course(self,info):
        return read_data()