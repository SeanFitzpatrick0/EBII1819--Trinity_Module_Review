from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from lecturers.models import Lecturer
from django.contrib.auth.models import User
from django.utils import timezone

DEFAULT_LECTURER_ID = 1

class Module(models.Model):
    code = models.CharField('The modules unique code', max_length=6, primary_key=True)
    name = models.CharField('The modules full name', max_length=100)
    lecturer = models.CharField('The modules lecturer', max_length=50)
    description = models.TextField('The description & learning outcomes of the module',max_length=2000)
    ects = models.PositiveIntegerField('The ECTS provided on completion of the module', validators=[MinValueValidator(5), MaxValueValidator(20)])

    def __str__(self):
        return "%s : %s" % (self.code, self.name)

class Module_Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Module, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=500)

    def __str__(self):
        return 'ID: %d,\tAuthor: %s,\tSubject: %s, Content:%s' % (self.pk, self.author, self.subject.name, self.content[0:50])


class Module_Rating(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    mesurement_title = models.CharField("Module Rating Title eg Usefulness", max_length=50)
    rating_value = models.PositiveIntegerField('Ratings', validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return 'Rating: %d' % (self.rating_value)
