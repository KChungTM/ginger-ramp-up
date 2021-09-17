import graphene
from graphene_django import DjangoObjectType
from .models import Restaurant

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'x',
            'y' ,
            'z',
            'category',
            'rating',
        )

class RestaurantInput(graphene.InputObjectType):
    name = graphene.String()
    x = graphene.Int()
    y = graphene.Int()
    z = graphene.Int()
    category = graphene.String()
    rating = graphene.Int()
    

class CreateRestaurant(graphene.Mutation):
    class Arguments:
        input = RestaurantInput(required=True)

    restaurant = graphene.Field(RestaurantType)

    @classmethod
    def mutate(cls, root, info, input):
        restaurant = Restaurant()
        restaurant.name = input.name
        restaurant.x = input.x
        restaurant.y = input.y
        restaurant.z = input.z
        restaurant.category = input.category
        restaurant.rating = input.rating
        restaurant.save()
        return CreateRestaurant(restaurant=restaurant)

class DeleteRestaurant(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    restaurant = graphene.Field(RestaurantType)

    @classmethod
    def mutate(cls, root, info, name):
        restaurant = Restaurant.objects.get(name = name)
        restaurant.delete()      

        return DeleteRestaurant(restaurant=restaurant) 

class GetRestaurants(graphene.Mutation):
    @classmethod
    def mutate(cls) :
        return Restaurant.objects.all()

class Query(graphene.ObjectType):
    restaurant = graphene.List(RestaurantType)

    def resolve_restaurant(root, info, **kwargs):
        # Querying a list
        return Restaurant.objects.all()

class Mutation(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
    delete_restaurant = DeleteRestaurant.Field()
    get_restaurants = GetRestaurants.Field()
        
schema = graphene.Schema(query=Query, mutation=Mutation)