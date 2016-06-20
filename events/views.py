from django.http import HttpResponse
from models import Event
from models import User
from models import Participant
from models import Like
import time
import json
import os
from datetime import datetime
from django.utils import timezone
from events import constants

query_template = ''


# Create your views here.
def list_all(request):

    token = request.GET.get('token')
    current_user = User.objects.get(token=token)
    list_id_list = []
    for like in Like.objects.filter(user=current_user):
        list_id_list.append(like.event.id)
    start_date = None
    end_date = None
    # capture all parameters
    page_index = request.GET.get('page_index', 0)
    page_size = request.GET.get('page_size',20)
    channel_id = request.GET.get('channel_id')
    if 'start_date' in request.GET:
        start_date = datetime.fromtimestamp((float)(request.GET['start_date'].__str__())).strftime('%Y-%m-%d %H:%M:%S')
    if 'end_date' in request.GET:
        end_date = datetime.fromtimestamp((float)(request.GET['end_date'].__str__())).strftime('%Y-%m-%d %H:%M:%S')

    # build query
    # read query template from file
    global query_template
    if query_template == '':
        dir_path = os.path.dirname(__file__) + '/raw_query/list_events.sql'
        file = open(dir_path, 'r')
        query_template = file.read()

    query = query_template
    if channel_id is not None:
        query = query + ' and ch.id = ' + channel_id
    if start_date is not None:
        query = query + ' and e.start_date >= ' + "'" + start_date + "'"
    if end_date is not None:
        query = query + ' and e.end_date <= ' + "'" + end_date + "'"
    query = query + ' GROUP BY e.id LIMIT ' + str(page_size) + ' OFFSET ' + str(page_index * page_size)
    # execute query
    event_list = Event.objects.raw(query)
    now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

    response_data_list = []
    for event in event_list:
        response_data = event.to_json()
        # extra info
        response_data['channel_name'] = event.channel_name
        response_data['channel_id'] = event.channel_id
        response_data['owner_id'] = event.owner_id
        response_data['owner_name'] = event.owner_name
        response_data['owner_avatar_id'] = event.owner_avatar_id
        if event.id in list_id_list:
            response_data['is_liked'] = True
        else:
            response_data['is_liked'] = False
        if event.startDate >= now:
            response_data['is_going'] = True
        else:
            response_data['is_going'] = False
        response_data['count_like'] = event.count_like
        response_data['count_participant'] = event.count_participant

        response_data_list.append(response_data)
    return HttpResponse(json.dumps(response_data_list), status=200, content_type="application/json")


def list_participant(request):
    id = request.GET['id']
    event = None
    response_data_list = []
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return HttpResponse(json.dumps({'error': constants.EVENT_NOT_FOUND}), status=500,
                            content_type="application/json")

    for participant in Participant.objects.filter(event=event):
        user = participant.user
        response_data_list.append(user.to_json())

    return HttpResponse(json.dumps(response_data_list), status=200, content_type="application/json")
