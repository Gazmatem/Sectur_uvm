from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    role = models.CharField(default="Estudiante", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "users"

    def __str__(self):
        return self.role


class Empresa(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="active")
    num_pais = models.IntegerField(default=0)
    pais = models.CharField(max_length=50, default="México")
    tamano = models.IntegerField(default=0)
    giro = models.CharField(max_length=500, default="active")
    antiguedad = models.IntegerField(default=0)
    razon_social = models.CharField(max_length=500, default="active")
    sitio_fisico = models.CharField(max_length=500, default="active")
    utilidades = models.IntegerField(default=0)
    num_entidad = models.IntegerField(default=0)
    entidad = models.CharField(max_length=50, default="active")
    fs_global = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "empresa"
        verbose_name = "empresa"
        verbose_name_plural = "empresas"

    def __str__(self):
        return self.nombre

class EvaluacionEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
    habilidad = models.CharField(max_length=500, default="active")
    puntaje = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "EvaluacionEmpresa"
        verbose_name = "EvaluacionEmpresa"
        verbose_name_plural = "EvaluacionEmpresa"

    def __str__(self):
        return self.habilidad


