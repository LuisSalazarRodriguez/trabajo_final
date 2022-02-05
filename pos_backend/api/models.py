from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorito(models.Model):
    favorito_id = models.AutoField(primary_key=True)
    favorito_titulo = models.CharField(max_length=100,verbose_name='titulo')
    favorito_url = models.CharField(max_length=200,verbose_name='url')
    favorito_fecha = models.DateTimeField(null=True,verbose_name='Fecha de registro')
    
    def __str__(self):
        return self.favorito_titulo
    
    
    
    
