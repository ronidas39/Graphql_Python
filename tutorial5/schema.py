import graphene


class weather(graphene.ObjectType):
    city=graphene.String()
    temperature=graphene.String()