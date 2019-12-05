import graphene

from project.board.schema import Query as boardQuery


class Query(boardQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
