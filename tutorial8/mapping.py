import graphene
from schema import footballplayer,cricketplayer
from data import read_data

class query(graphene.ObjectType):
    class Meta:
        name="interfacequery"
        description="list with interface"
    fplayer=graphene.List(footballplayer,description="list object type implements interface")
    def resolve_fplayer(self,info):
        data=read_data()
        return data[0]["footballplayer"]
    
    cplayer=graphene.List(cricketplayer,description="list object type implements interface")
    def resolve_cplayer(self,info):
        data=read_data()
        return data[0]["cricketplayer"]