from ...vendor import models


def resolve_vendors(info):
    user = info.context.user
    if user:
        return user.vendors.all()
    else:
        models.Vendor.objects.all()
