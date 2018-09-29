from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Module(models.Model):
    code = models.CharField(max_length=6)
    name = models.TextField(max_length=100)
    lecturer = models.TextField(max_length=50)
    ects = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(20)])

    def __str__(self):
        return "%s : %s" % (self.code, self.name) 
