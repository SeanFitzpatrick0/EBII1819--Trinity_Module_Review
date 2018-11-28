from modules.models import Module
Module.objects.all().delete()
print(Module.objects.all())