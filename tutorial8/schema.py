import graphene

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