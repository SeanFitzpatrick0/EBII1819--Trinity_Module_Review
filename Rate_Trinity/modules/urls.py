from django.conf.urls import url
from . import views
from modules.models import Module, Module_Comment
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Module.objects.all().order_by('code'),
                                template_name='modules/modulesList.html'), name='module_list'),
    url(r'^(?P<pk>[^/]+)$', DetailView.as_view(model=Module, template_name='modules/viewModule.html'), name='module_view')
]