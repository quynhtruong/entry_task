from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from models import User
import json


# Create your views here.
def list_all(request):
    users = User.objects.all()
    data = serializers.serialize('json', users)
    return HttpResponse(json.dumps(data), content_type="application/json")
