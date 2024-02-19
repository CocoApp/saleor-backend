import graphene
from .types import Vendor
from .resolvers import resolve_vendors
from .mutations.vendor_create import VendorCreate


class VendorQueries(graphene.ObjectType):
    vendors = graphene.List(
        Vendor,
    )

    def resolve_vendors(_root, info):
        return resolve_vendors(info)


class VendorMutations(graphene.ObjectType):
    create_vendor = VendorCreate.Field()
