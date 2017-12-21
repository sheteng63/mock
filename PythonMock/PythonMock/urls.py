from django.conf.urls import url
from . import view
from . import mockdb

urlpatterns = [
    url(r'^addNewUrl$', mockdb.addDb),
    url(r'^updateForm$', mockdb.updateForm),
    url(r'^updateUrl$', mockdb.updateDb),
    url(r'^deleteUrl$', mockdb.deleteDb),
    url(r'^queryUrl$', mockdb.queryAll),
    # url(r'^robot/api/user/login$', mockdb.login),
    url(r'^', mockdb.query)

]
