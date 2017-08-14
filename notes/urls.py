from django.conf.urls import url

from . import views

app_name = 'notes'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_note/$', views.add_note, name='add_note'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<pk>.*)/$', views.ShowNote.as_view(), name='show_note'),
]
