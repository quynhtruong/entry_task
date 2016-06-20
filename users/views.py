import json

import time
import uuid
import pytz

from events import constants
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
from events.models import User
from datetime import datetime, timedelta


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        users = User.objects.filter(email=email, password=password)
        # user not found -> return error
        if not users.exists():
            return HttpResponse(json.dumps(constants.USER_NOT_FOUND), status=404, content_type="application/json")
        else:
            user = users[0]
            now = datetime.utcnow()
            now = now.replace(tzinfo=pytz.utc)
            # if token has been expired, active new one
            if (user.token == '' or user.tokenExpiredOn == None or user.tokenExpiredOn < now):
                user.token = uuid.uuid4().__str__()
                user.tokenExpiredOn = datetime.now() + timedelta(hours=24)
                user.save()
            # generate json response
            responseData = {}
            responseData['email'] = user.email
            responseData['password'] = user.password
            responseData['token'] = user.token
            responseData['tokenExpiredOn'] = time.mktime(user.tokenExpiredOn.timetuple())

            return HttpResponse(json.dumps(responseData), status=200, content_type="application/json")
