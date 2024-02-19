import graphene
from .types import Vendor
from .resolvers import resolve_vendors


class VendorQueries(graphene.ObjectType):
    vendors = graphene.List(
        Vendor,
    )

    def resolve_vendors(_root, info):
        return resolve_vendors(info)
