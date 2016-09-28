from django.conf.urls import url, include
from jobs import views

# import api lib for routes

urlpatterns = [

    '''url(r'^profiles/index$', views.profiles_index, name='profiles-index'),
    url(r'^profiles/new/$', views.profiles_new, name='profiles-new'),
    url(r'^profiles/edit/(\d+)/$', views.profiles_edit, name='profiles-edit'),
    url(r'^profiles/show/(\d+)/$', views.profiles_show, name='profiles-show'),
    url(r'^profiles/delete/(\d+)/$', views.profiles_show, name='profiles-delete'),
    '''
]
