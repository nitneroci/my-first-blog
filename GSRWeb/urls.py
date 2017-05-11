from django.conf.urls import url

from . import views
"""
Les urls de redirection, un redirige à la fonction qui correspond
La redirection se fait en fonction de ce qui est après le : http://.../GSRWeb/?, là ou est le '?'
"""
urlpatterns = [
    url(r'^$', views.index, name='index'),#Si le '?' = '' alors ou redirige vers index
    url(r'^query', views.executeQuery, name='executeQuery'),#Si le '?' = 'query' alors ou redirige vers executeQuery, cela sert au JSON
    url(r'^recup', views.recupDonnee, name='recupDonnee'),#Si le '?' = 'recup' alors ou redirige vers recupDonnee, cela sert au JSON
]
