from django.conf.urls import url
from . import view
from . import mockdb

urlpatterns = [
    url(r'^$',view.hello),
    url(r'^addNewUrl$', mockdb.testdb)
]
