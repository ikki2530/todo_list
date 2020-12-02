from django.db import models

# Create your models here.
class TareasCampos(models.Model):
    """
    Atributos para las tareas de los desarrolladores
    """
    titulo = models.CharField(max_length=32)
    descripcion = models.TextField()
    tiempo_estimado = models.IntegerField(default=0)
    tiempo_trabajado = models.FloatField(default=0.0)
    latitud = models.FloatField(default=0.0)
    longitud = models.FloatField(default=0.0)
