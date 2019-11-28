from django.conf.urls import url

from .views import (PokeList)
from .views.pokemon import (TimeCreate, TimeList)

urlpatterns = [
    url(r'pokes/$', PokeList.as_view()),
    url(r'pokes/(?P<pk>\d+)/$', PokeList.as_view()),
    url(r'time/add/$', TimeCreate.as_view()),
    url(r'time/$', TimeList.as_view()),

]
