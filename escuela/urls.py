from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from escuela import views

urlpatterns = [
    url(r'^snippets/$', views.EstudianteList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.EstudianteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)