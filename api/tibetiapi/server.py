import graphene
import responder


api = responder.API()


class Starship(graphene.ObjectType):
    name = graphene.String()


class Character(graphene.Interface):
    id = graphene.ID()
    name = graphene.String()
    friends = graphene.List(lambda: Character)


class Human(graphene.ObjectType):
    class Meta:
        interfaces = (Character,)

    starships = graphene.List(Starship)
    home_planet = graphene.String()


class Droid(graphene.ObjectType):
    class Meta:
        interfaces = (Character,)

    primary_function = graphene.String()


class Query(graphene.ObjectType):
    hero = graphene.Field(Character, episode=graphene.Int())

    # pylint: disable=no-self-argument,no-self-use
    def resolve_hero(root, _info, episode):  # noqa: N805
        if episode == 5:
            return Human(name="L S", home_planet="Tat")
        return Droid(name="R D")


schema = graphene.Schema(query=Query, types=[Human, Droid])
view = responder.ext.GraphQLView(api=api, schema=schema)

api.add_route("/graph", view)
