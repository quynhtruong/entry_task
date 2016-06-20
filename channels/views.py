from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
# Create your views here.
import json
import time
from events.models import  Channel

def list(request):

    response_data_list = []
    for channel in Channel.objects.all():
        response_data  = {}
        response_data['id'] = channel.id
        response_data['name'] = channel.name
        response_data['createdDate'] = time.mktime(channel.created_date.timetuple())
        response_data['updatedDate'] = time.mktime(channel.updated_date.timetuple())
        response_data_list.append(response_data)
    return HttpResponse(json.dumps(response_data_list), content_type="application/json")
