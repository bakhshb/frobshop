from oscar.apps.shipping import repository, methods, models
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal as D

class Standard(methods.FixedPrice):
    code = 'standard'
    name = 'Standard shipping'
    charge_excl_tax = D('5.00')

class Express(methods.FixedPrice):
    code = "express"
    name = "USPS Priority Mail"
    charge_excl_tax = D('24.99')


class Repository(repository.Repository):
	def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
		methods = []
		methods.extend(list(models.OrderAndItemCharges.objects.all()))
		return methods