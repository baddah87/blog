from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^test/$', views.org_members,name="test"),
    url(r'^list/$', views.list_repo,name="list"),

]