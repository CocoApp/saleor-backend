from ....vendor import models
from ....account.models import User
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

    @classmethod
    def clean_input(cls, info, instance, data, **kwargs):
        cleaned_input = super().clean_input(info, instance, data, **kwargs)
        cleaned_input["owner"] = User.objects.get(id=cleaned_input["owner_id"])
        return cleaned_input
