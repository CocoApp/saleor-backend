from ...vendor import models


def resolve_vendors(info):
    user = info.context.user
    return models.Vendor.objects.all()
    if user:
        return user.vendors.all()
    else:
        return models.Vendor.objects.all()
