from django.conf.urls import url
from . import views
from lecturers.models import Lecturer
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Lecturer.objects.all().order_by('name'),
                                template_name='lecturers/lecturersList.html'), name='lecturers_list'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Lecturer,
                                            template_name='lecturers/viewLecturer.html'), name='lecturer_view')
]