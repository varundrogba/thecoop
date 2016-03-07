from tastypie.resources import ModelResource
from billing.models import Billing

class BillingResource(ModelResource):
    class Meta:
        queryset = Billing.objects.all()
        resource_name = 'billing'
