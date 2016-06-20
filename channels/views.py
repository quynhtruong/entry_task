from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
import json
import time
from events.models import  Channel

def list(request):

    responseDataList = []
    for channel in Channel.objects.all():
        responseData  = {}
        responseData['id'] = channel.id
        responseData['name'] = channel.name
        responseData['createdDate'] = time.mktime(channel.createdDate.timetuple())
        responseData['updatedDate'] = time.mktime(channel.updatedDate.timetuple())
        responseDataList.append(responseData)
    return HttpResponse(json.dumps(responseDataList), content_type="application/json")
