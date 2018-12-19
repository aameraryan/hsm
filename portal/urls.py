from django.conf.urls import url
from . import views

app_name = 'portal'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^screen_request/$', views.screen_request, name='screen_request'),
    url(r'^display_screen/(?P<floor_id>[0-9]+)/$', views.display_screen, name='display_screen'),
    url(r'^floor_list/$', views.floor_list, name='floor_list')

]
