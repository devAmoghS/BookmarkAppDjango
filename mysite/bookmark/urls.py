from django.conf.urls import url
from bookmark import views as bookmark_views

urlpatterns = [
  url(r'^user/(?P<username>[-\w]+)/$', bookmark_views.bookmark_user, name='app_bookmark_user'),
  url(r'^create/$', bookmark_views.bookmark_create, name='bookmark_bookmark_create'),
  url(r'^edit/(?P<pk>\d+)/$', bookmark_views.bookmark_edit, name='bookmark_bookmark_edit'),
  url(r'^$', bookmark_views.bookmark_list, name='app_bookmark_list'),
]
