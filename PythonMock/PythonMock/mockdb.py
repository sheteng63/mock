from django.http import HttpResponse

from mockapi.models import MockData
import os

# 数据库操作
def testdb(request):
    test1 = MockData(urlname=request.GET["urlName"])
    print("urlName = %s "  % request.GET["urlName"])
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
