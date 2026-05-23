from django.db import models
from django.conf import settings
import uuid

class WorkExperiences(models.Model):
    """
    Experiencias laborales de un usuario.
    Relaciona: Usuario y Puesto de Trabajo (JobTitle)
    """
    work_experience_id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    # Datos de la empresa
    enterprise_name = models.CharField(
        max_length=255, 
        verbose_name="Nombre de la Empresa"
    )
    
    # Responsabilidades y descripción
    responsibilities = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Responsabilidades"
    )
    
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Descripción general"
    )
    
    achievement = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Logros alcanzados"
    )
    
    # Fechas del período laboral
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(
        null=True, 
        blank=True, 
        verbose_name="Fecha de finalización", 
        help_text="Dejar en blanco si es empleo actual"
    )
    
    # Auditoría
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    # Relaciones
    job_title_id = models.ForeignKey(
        'JobTitle', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='job_title_id', 
        verbose_name="Puesto de Trabajo"
    )

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        db_column='user_id', 
        verbose_name="Usuario", 
        related_name='work_experiences'
    )

    class Meta:
        db_table = 'work_experiences'
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencias Laborales'
        ordering = ['-start_date', 'user_id']

    def __str__(self):
        return f"{self.user_id} - {self.enterprise_name} ({self.start_date})"

    @property
    def is_current_job(self):
        """Propiedad para verificar si es el empleo actual"""
        return self.end_date is None

    @classmethod
    def create(cls, enterprise_name, start_date, end_date=None, description=None, 
               job_title_id=None, user_id=None, achievement=None):
        """Método de fábrica para crear una experiencia laboral"""
        return cls(
            enterprise_name=enterprise_name,
            start_date=start_date,
            end_date=end_date,
            description=description,
            job_title_id=job_title_id,
            user_id=user_id,
            achievement=achievement
        )