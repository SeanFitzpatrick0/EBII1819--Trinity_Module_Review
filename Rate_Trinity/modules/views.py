from django.shortcuts import render, redirect
from modules.models import Module, Module_Comment
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .forms import Module_Comment_Form
from ML_API import ml
import csv , io

def index(request):
    return render(request, 'modules/modulesList.html')

class ModuleDetailView(DetailView):
    context_object_name = 'module'
    model = Module
    form_class = Module_Comment_Form
    template_name='modules/viewModule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Module_Comment.objects.filter(subject_id=context['module'].pk)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        
        print(ml.isAbusiveComment('What a prick'))

        form = self.form_class(request.POST)
        form.instance.author = self.request.user
        form.instance.subject = Module.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            comment = form.save()
            request.user.profile.comments.add(comment)

        form = self.form_class
        return redirect('module_view', kwargs['pk'])

@permission_required('admin.can_add_log_entry')
def module_csv_upload(request):
    template = 'modules/module_csv_upload.html'
    context = {
        'order' : 'Order of the CSV must be: code, name, lecturer, description, ects'
    }

    if request.method == 'GET':
        return render(request, template_name = template, context=context)

    csv_file = request.FILES['file']
    if not '.csv' in csv_file.name:
        messages.error(request, 'This file is not a .csv file')
        return render(request, template_name = template, context=context)
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string) #Skip header

    #Read data
    for column in csv.reader(io_string, delimiter=','):
        try:
            print(column)
            _, created = Module.objects.update_or_create(
                code=column[0],
                name=column[1],
                lecturer=column[2],
                description=column[3],
                ects=column[4]
            )
        except:
           print('Error while adding ' + str(column))
    return render(request, template)
