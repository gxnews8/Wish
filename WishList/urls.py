from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^dashboard$', views.index, name = 'dashboard'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^logIn$', views.logIn, name = 'logIn'),
    url(r'^addWish$', views.addWish, name = 'addWish'),
    url(r'^delWish$', views.delWish, name = 'delWish'),
    url(r'^mvWish$', views.mvWish, name = 'mvWish'),
    url(r'^logOut$', views.logOut, name = 'logOut'),
]
