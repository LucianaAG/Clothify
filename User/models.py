from django.db import models

# Create your models here.


class User(models.Model):
    Name = models.CharField('Nombre',unique = True, max_length=100)
    last_name = models.CharField('Apellido',unique = True, max_length=100)
    email = models.EmailField('Correo', max_length=254,unique = True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200,blank = True,null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
