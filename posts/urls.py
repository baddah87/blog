from django.conf.urls import url
# put . instead of posts if i am in the same file#

from . import views

urlpatterns = [
	url(r'^list/$', views.post_list, name="list"),
    url(r'^detail/(?P<post_id>\d+)$', views.post_detail, name="detail"),
    
   
    
]