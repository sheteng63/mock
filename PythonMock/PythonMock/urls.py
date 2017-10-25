from django.conf.urls import url
from . import view
from . import mockdb

urlpatterns = [
    url(r'^',mockdb.query),
    url(r'^addNewUrl$', mockdb.addDb),
    url(r'^updateUrl$',mockdb.updateDb),
    url(r'^deleteUrl$',mockdb.deleteDb),
    url(r'^queryUrl$', mockdb.queryAll)
]
