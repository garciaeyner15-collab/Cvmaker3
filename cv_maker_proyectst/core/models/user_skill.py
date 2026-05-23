from django.db import models
from django.conf import settings
import uuid

class UserSkill(models.Model):
    user_skill_id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    # Relaciones
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        db_column='user_id', 
        verbose_name="Usuario",
        related_name='user_skills'
    )
    skill_id = models.ForeignKey(
        'Skill', 
        on_delete=models.PROTECT, 
        db_column='skill_id', 
        verbose_name="Habilidad"
    )
    
    # Nivel de la habilidad
    level = models.CharField(
        max_length=50, 
        verbose_name="Nivel",
        help_text="Ej: Principiante, Intermedio, Avanzado, Experto"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'user_skill'
        verbose_name = 'Habilidad de Usuario'
        verbose_name_plural = 'Habilidades de Usuarios'
        # Evita que un usuario registre la misma habilidad más de una vez
        unique_together = [['user_id', 'skill_id']]

    def __str__(self):
        return f"{self.user_id} - {self.skill_id} ({self.level})"

        