import graphene
from schema import emp
from data import read_file

class query(graphene.ObjectType):
    employee=graphene.List(emp)
    def resolve_employee(self,info):
        return read_file()