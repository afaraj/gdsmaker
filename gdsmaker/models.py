from django.db import models

# Create your models here.
class GDS(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(blank=True, default='')
    frozen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title