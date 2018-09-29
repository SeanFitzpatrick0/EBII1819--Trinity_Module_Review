from django.conf.urls import url
from . import views
from modules.models import Module
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Module.objects.all().order_by('code'),
                                template_name='modules/modulesList.html'))
]