import graphene
from graphene import String
from schema import player
from data import read_data

class query(graphene.ObjectType):
    player=graphene.List(player,required=True,playertype=String(required=True))
    def resolve_player(self,info,playertype):
        data=read_data()
        if playertype=="fplayer":
            return data[0]["footballplayer"]
        elif playertype=="cplayer":
            return data[0]["cricketplayer"]
        else:
            return data[0]["invalid"]
        

