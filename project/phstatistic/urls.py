from django.conf.urls import patterns, include, url

from phstatistic import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^create/$', views.create, name='create'),
    url(r'^timehunt/$', views.timehunt, name='timehunt'),
    url(r'^detail/$', views.detail, name='detail'),

    url(r'^$', views.index, name='index'),


)
