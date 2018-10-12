from django.conf.urls import url
from . import views
from modules.models import Module, Module_Comment
from django.views.generic import ListView, DetailView

class ModuleDetailView(DetailView):
    context_object_name = 'module'
    model = Module
    template_name='modules/viewModule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Module_Comment.objects.filter(subject_id=context['module'].pk)
        return context

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Module.objects.all().order_by('code'),
                                template_name='modules/modulesList.html'), name='module_list'),
    url(r'^(?P<pk>[^/]+)$', ModuleDetailView.as_view(), name='module_view')
]