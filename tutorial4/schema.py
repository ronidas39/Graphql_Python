import graphene

class emp(graphene.ObjectType):
    name=graphene.String()
    city=graphene.String()
    designation=graphene.String()
    experience_in_year=graphene.String()