from django.db import models

class Redsocial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    link = models.URLField(verbose_name="Enlace", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "red social"
        verbose_name_plural = "redes sociales"
        ordering = ['name']

    def __str__(self):
        return self.name