from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Collection)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.Product)

class ProductAdmin():
    pass

