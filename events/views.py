from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from models import Event
from models import User
from models import Participant
from models import Like
import time
import json
import os
from datetime import  datetime
from django.utils import timezone

queryTemplate = ''
# Create your views here.
def list_all(request):
    # capture all parameters
    token = request.GET['token']
    currentUser = User.objects.get(token=token)
    listIdList = []
    for like in Like.objects.filter(user=currentUser):
        listIdList.append(like.event.id)
    pageSize = 20
    pageIndex = 0
    channelId = None
    startDate = None
    endDate = None
    if 'pageIndex' in request.GET:
        pageIndex = request.GET['pageIndex']
    if 'pageSize' in request.GET:
        pageSize = request.GET['pageSize']
    if 'channelId' in request.GET:
        channelId = request.GET['channelId']
    if 'startDate' in request.GET:
        startDate = datetime.fromtimestamp((float)(request.GET['startDate'].__str__())).strftime('%Y-%m-%d %H:%M:%S')
    if 'endDate' in  request.GET:
        endDate = datetime.fromtimestamp((float)(request.GET['endDate'].__str__())).strftime('%Y-%m-%d %H:%M:%S')

    # build query
    #read query template from file
    global queryTemplate
    if queryTemplate == '':
        dirPath = os.path.dirname(__file__) + '/raw_query/list_events.sql'
        file = open(dirPath, 'r')
        queryTemplate = file.read()

    query = queryTemplate
    if channelId is not None:
        query = query + ' and ch.id = '+channelId
    if startDate is not None:
        query = query+ ' and e.start_date >= '+ "'"+startDate+"'"
    if endDate is not None:
        query = query+ ' and e.end_date <= '+ "'"+endDate+"'"
    query = query+' GROUP BY e.id LIMIT '+str(pageSize)+' OFFSET '+ str(pageIndex*pageSize)
    #execute query
    eventList = Event.objects.raw(query)
    now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

    responseDataList = []
    for event in eventList:
        responseData = {}
        responseData['id'] = event.id
        responseData['title'] = event.title
        responseData['startDate'] = time.mktime(event.startDate.timetuple())
        responseData['endDate'] = time.mktime(event.endDate.timetuple())
        responseData['createdDate'] = time.mktime(event.createdDate.timetuple())
        responseData['description'] = event.description
        responseData['avatarID'] = event.avatarId

        responseData['channelName'] = event.channel_name
        responseData['channelId'] = event.channel_id

        responseData['creatorId'] = event.owner_id
        responseData['creatorName'] = event.owner_name
        responseData['creatorAvatarId'] = event.owner_avatar_id
        if event.id in listIdList:
            responseData['isLiked']  = True
        else:
            responseData['isLiked'] = False
        if event.startDate >= now:
            responseData['isGoing'] = True
        else:
            responseData['isGoing'] = False
        responseData['numberLike'] = event.count_like
        responseData['numberParticipant'] = event.count_participant

        responseDataList.append(responseData)
    return HttpResponse(json.dumps(responseDataList), status=200, content_type="application/json")


