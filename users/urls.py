from django.conf.urls import url, include
from users import views
# import api lib for routes

urlpatterns = [

    url(r'^profiles/index$', views.profiles_index, name='profiles-index'),
    url(r'^profiles/new/$', views.profiles_new, name='profiles-new'),
    url(r'^profiles/edit/(\d+)/$', views.profiles_edit, name='profiles-edit'),
    url(r'^profiles/show/(\d+)/$', views.profiles_show, name='profiles-show'),
    url(r'^profiles/delete/(\d+)/$', views.profiles_show, name='profiles-delete'),

    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^private/$', views.private, name='private'),
]