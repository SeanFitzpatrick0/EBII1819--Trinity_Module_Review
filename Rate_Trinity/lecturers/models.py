from django.db import models

class Lecturer(models.Model):
    name = models.CharField('The Lecturers full name with no professional title', max_length=100)
    school = models.CharField('The school the lecture works in', max_length=100)

    def __str__(self):
        return "%s : %s" % (self.name, self.school) 
