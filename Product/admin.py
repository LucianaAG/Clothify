from django.contrib import admin
from Product.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(Carrito)
admin.site.register(ProductSize)
