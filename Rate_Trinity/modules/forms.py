from django.forms import ModelForm
from . models import Module_Comment

class Module_Comment_Form(ModelForm):
    class Meta:
        model = Module_Comment
        fields = ['content']