from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from lecturers.models import Lecturer

DEFAULT_LECTURER_ID = 1

class Module(models.Model):
    code = models.CharField('The modules unique code', max_length=6, primary_key=True)
    name = models.CharField('The modules full name', max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, default=DEFAULT_LECTURER_ID)
    description = models.TextField('The description & learning outcomes of the module',max_length=2000)
    ects = models.PositiveIntegerField('The ECTS provided on completion of the module', validators=[MinValueValidator(5), MaxValueValidator(20)])

    def __str__(self):
        return "%s : %s" % (self.code, self.name) 
