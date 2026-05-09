from django.db import models


class JobTitle(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'job_titles'
        verbose_name = 'Job Title'
        verbose_name_plural = 'Job Titles'
     
    def __str__(self):
        return self.title