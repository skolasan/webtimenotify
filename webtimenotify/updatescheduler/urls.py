from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'submittask', views.submittask, name='submittask'),
    url(r'api/deletetask', views.deletetask, name='deletetask'),
    url(r'api/getpendingentries', views.getpendingentries, name='getpendingentries'),
]
