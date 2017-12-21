from django.http import HttpResponse

from mockapi.models import MockData
import os
import json
from django.shortcuts import render


# 数据库操作
# 添加
def addDb(request):
    resp = {'code': 0, 'msg': '', 'content': ''}
    list = MockData.objects.all()
    for mock in list:
        if mock.urlName == request.GET["urlName"]:
            resp['msg'] = '不能重复添加'
            return HttpResponse(json.dumps(resp), content_type="application/json")
    test = MockData(urlName=request.GET["urlName"], urlType=request.GET['urlType'],
                    urlResponse=request.GET['urlResponse'])
    test.save()
    return queryAll(request)


# 修改
def updateDb(request):
    test = MockData.objects.get(id=request.GET['id'])
    test.urlName = request.GET["urlName"]
    test.urlType = request.GET["urlType"]
    test.urlResponse = request.GET["urlResponse"]
    test.save()
    return queryAll(request)


def updateForm(request):
    mock = MockData.objects.get(id=request.GET['id'])
    context = {'id': mock.id, 'urlName': mock.urlName, 'urlType': mock.urlType, 'urlResponse': mock.urlResponse}
    print('mockResPonse = %s' % mock.urlResponse)
    return render(request, 'update_form.html', context)


# 删除
def deleteDb(request):
    test = MockData.objects.get(id=request.GET['id'])
    test.delete()
    return queryAll(request)


# 查询所有
def queryAll(request):
    list = MockData.objects.all()
    mockList = []
    for mock in list:
        mockjson = {'id': mock.id, 'urlName': mock.urlName, 'urlType': mock.urlType, 'urlResponse': mock.urlResponse}
        mockList.append(mockjson)
    print("mockJson = %s" % mockList)
    context = {'code': 0, 'msg': '', 'content': mockList}
    return render(request, 'hello.html', context)


#


def query(request):
    baseResp = {'code': 1, 'msg': '请求类型错误', 'content': ''}
    print("urlName = %s" % request.path)
    response = MockData.objects.get(urlName=request.path)
    resp = response.urlResponse
    urlType = response.urlType

    print("response = %s" % resp)

    return HttpResponse(resp, content_type="application/json")


def login(request):
    baseResp = {
        "status": 1,
        "msg": "",
        "token": "令牌"
    }

    return HttpResponse(json.dumps(baseResp), content_type="application/json")
