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
        response_data_list.append(channel.to_json())
    return HttpResponse(json.dumps(response_data_list), content_type="application/json")
