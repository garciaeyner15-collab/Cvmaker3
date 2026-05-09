from django.db import models
from django.conf import settings
import uuid

class UserLanguage(models.Model):
    user_language_id = models.AutoField(primary_key=True)
    external_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    # Relaciones
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        db_column='user_id', 
        verbose_name="Usuario",
        related_name='user_languages'
    )
    language_id = models.ForeignKey(
        'Languages', 
        on_delete=models.PROTECT, 
        db_column='language_id', 
        verbose_name="Idioma"
    )
    
    # Nivel de dominio (según documento)
    level = models.CharField(
        max_length=50, 
        verbose_name="Nivel de dominio",
        help_text="Ej: Nativo, Avanzado, Intermedio, Básico"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'user_language'
        verbose_name = 'Idioma de Usuario'
        verbose_name_plural = 'Idiomas de Usuarios'
        # Un usuario no debería tener el mismo idioma duplicado
        unique_together = [['user_id', 'language_id']]

    def __str__(self):
        return f"{self.user_id} - {self.language_id} ({self.level})"
        