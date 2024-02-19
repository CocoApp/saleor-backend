from ....vendor import models
from ...core.mutations import ModelMutation
from ..types import VendorCreateInput, Vendor
from ...core.types import VendorError


class VendorCreate(ModelMutation):
    class Arguments:
        input = VendorCreateInput(
            required=True, description="Fields required to create vendor."
        )

    class Meta:
        description = "Creates new vendor."
        model = models.Vendor
        object_type = Vendor
        error_type_class = VendorError
        error_type_field = "vendors_errors"
