from django.conf.urls import url
from . import views
from modules.models import Module, Module_Comment
from django.views.generic import ListView, DetailView
from .views import ModuleDetailView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Module.objects.all().order_by('code'),
                                template_name='modules/modulesList.html'), name='module_list'),
    url(r'^(?P<pk>\w+?)/$', ModuleDetailView.as_view(), name='module_view'),
    url('upload-csv/', views.module_csv_upload, name='module_csv_upload')
]