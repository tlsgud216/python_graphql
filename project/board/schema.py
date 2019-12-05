import graphene

from graphene_django.types import DjangoObjectType

from project.board.models import Category, Notice


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class NoticeType(DjangoObjectType):
    class Meta:
        model = Notice


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_notices = graphene.List(NoticeType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_notices(self, info, **kwargs):
        return Notice.objects.select_related('category').all()
