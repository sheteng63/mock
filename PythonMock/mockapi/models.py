from django.db import models


class MockData(models.Model):
    urlName = models.CharField(max_length=20) ## name of url
    urlType = models.CharField(max_length=5)  ## type of url
    urlResponse = models.CharField(max_length=1000) ## response of url
