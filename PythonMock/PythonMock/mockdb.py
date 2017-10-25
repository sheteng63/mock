from django.http import HttpResponse

from mockapi.models import MockData
import os

# 数据库操作
#添加
def addDb(request):

    test = MockData(urlname=request.GET["urlName"])
    print("urlName = %s "  % request.GET["urlName"])
    print("path = %s "  % request.path)
    test.save()
    return HttpResponse("<p>数据添加成功！</p>")
#修改
def updateDb(request):
    test = MockData.object.get(id = request.GET['id'])
    test.urlname = request.GET["urlName"]
    test.urlType = request.GET["urlType"]
    test.urlResponse = request.GET["urlResponse"]
    test.save()
    return HttpResponse("<p>数据修改成功！</p>")

#删除
def deleteDb(request):
    test = MockData.object.get(id = request.GET['id'])
    test.delete()
    return HttpResponse("<p>删除成功</p>")

#查询所有
def queryAll(request):
    list = MockData.object.all()
    print("lsit = %s" % list)

#
def query(request):
    response = MockData.object.get(urlname = request.path)
    res = response.urlResponse
    return HttpResponse("<p>查询成功</p>")