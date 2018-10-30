from django.shortcuts import render, redirect
from modules.models import Module, Module_Comment
from django.views.generic import ListView, DetailView
from .forms import Module_Comment_Form

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
        form = self.form_class(request.POST)
        form.instance.author = self.request.user
        form.instance.subject = Module.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            form.save()

        form = self.form_class
        return redirect('module_view', kwargs['pk'])