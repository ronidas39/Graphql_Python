import graphene
from graphene import String
class player(graphene.Interface):
    name=String()
    country=String()
    type=String()
    @classmethod
    def resolve_type(cls, instance, info):
        if(instance["type"]=="footballplayer"):
         return footballplayer
        elif(instance["type"]=="cricketplayer"):
         return cricketplayer
        else:
            return invalid
         

class footballplayer(graphene.ObjectType):
    class Meta:
        interfaces=(player,)
    position=String()

class cricketplayer(graphene.ObjectType):
    class Meta:
        interfaces=(player,)
    battingorder=String()

class invalid(graphene.ObjectType):
    class Meta:
        interfaces=(player,)
    invalid_data=String()
