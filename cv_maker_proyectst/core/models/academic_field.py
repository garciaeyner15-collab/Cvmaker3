from django.db import models
import uuid

class AcademicField(models.Model):
    academic_field_id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Descripción",
        help_text="Nombre del campo académico (ej. Ingeniería de Sistemas)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Fecha de actualización")

    class Meta:
        db_table = 'academic_field'
        verbose_name = 'Campo Académico'
        verbose_name_plural = 'Campos Académicos'
        ordering = ['description']

    def __str__(self):
        return self.description

    @classmethod
    def create(cls, description):
        return cls(description=description)