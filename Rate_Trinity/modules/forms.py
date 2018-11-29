from django.forms import ModelForm
from . models import Module_Comment

class Module_Comment_Form(ModelForm):

    def __init__(self, *args, **kwargs): 
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''

    class Meta:
        model = Module_Comment
        fields = ['content']