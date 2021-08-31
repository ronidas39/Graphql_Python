import graphene
from schema import weather
from data import read_data

class query(graphene.ObjectType):
    city_temp=graphene.Field(weather,city=graphene.String())
    def resolve_city_temp(self,info,city):
        data=read_data()
        for row in data:
            if row["city"]==city:
                return row
        return {
            "city":city,
            "temperature":"not found in the sequence"
        }


        