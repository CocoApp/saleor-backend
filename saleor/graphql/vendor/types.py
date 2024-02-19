import graphene
from ...vendor import models
from ..core.types import ModelObjectType, BaseInputObjectType


class Vendor(ModelObjectType[models.Vendor]):
    id = graphene.GlobalID(required=True, description="The ID of the vendor.")
    name = graphene.String(required=True, description="The name of the vendor.")
    description = graphene.String(
        required=True, description="The description of the vendor."
    )
    owner = graphene.String(required=True, description="The owner of the vendor.")
    phone_number = graphene.String(
        required=True, description="The phone_number of the vendor."
    )
    address = graphene.String(required=True, description="The address of the vendor.")
    website = graphene.String(required=True, description="The website of the vendor.")
    logo = graphene.String(required=True, description="The logo of the vendor.")
    created_at = graphene.DateTime(
        required=False, description="The created_at of the vendor."
    )
    updated_at = graphene.DateTime(
        required=False, description="The updated_at of the vendor."
    )

    class Meta:
        model = models.Vendor


class VendorCreateInput(BaseInputObjectType):
    name = graphene.String(description="Vendor name.", required=True)
    description = graphene.String(
        required=True, description="The description of the vendor."
    )
    phone_number = graphene.String(
        required=True, description="The phone_number of the vendor."
    )
    address = graphene.String(required=True, description="The address of the vendor.")
    website = graphene.String(required=True, description="The website of the vendor.")
