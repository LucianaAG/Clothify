from django.db import models
from User.models import User

# Create your models here.


class Carrito(models.Model):
    """ 
       A cada carrito le corresponde un usuario
    
    """
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=20, choices=(
        ('Activo'),
        ('Pendiente de pago'),
        ('Completado')
    ))

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

    def __str__(self):
        return f'{self.cliente}'

class CategoryProduct(models.Model):
    category = models.CharField('Category', max_length=20, choices=(
        ('Shirts'),
        ('Shorts'),
        ('Jumper'),
        ('Shoes'),
        ('coats')
    ))

    class Meta:
        verbose_name = "Categoria de producto"
        verbose_name_plural = "Categorias de productos"

    def __str__(self):
        return f'{self.category}'


class Product(models.Model):
    """
       A cada producto le corresponde una categoria.
       Cada producto se vincula a un carrito.
    
    """
    product_name = models.CharField('Product name', max_length=50, null=False, blank=False)
    description = models.TextField('Product description',max_length=200, null=False, blank=True)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    image = models.ImageField('Product image', upload_to='products/')
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f'{self.product_name}'

class ProductSize(models.Model):
    """
        A cada prenda le corresponde un tamaño.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField('Product size', max_length=20, choices=(
        ('XS'),
        ('S'),
        ('M'),
        ('L'),
        ('XL')
    ))

    class Meta:
        verbose_name = "Talle del producto"
        verbose_name_plural = "Talles de los productos"

    def __str__(self):
        return f'{self.size}'