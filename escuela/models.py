from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
    
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
    
    
class Estudiante(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100, blank=True, default='')
    apellido = models.CharField(max_length=200, blank=True)
    cedula = models.CharField(max_length=200, blank=True)
    ciudad = models.CharField(max_length=200, blank=True)
    provincia = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return '%s | %s | %s | %s | %s | %s' % (self.created, self.nombre, self.apellido, self.cedula, self.ciudad, self.provincia)

    class Meta:
        ordering = ('created',)