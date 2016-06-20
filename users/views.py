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
        # users = User.objects.raw('select u.id, count(DISTINCT c.id) as count_c from user_account_tab as u
        # INNER JOIN comment_tab as c on c.user_id = u.id where u.email = %s and u.password = %s GROUP by u.id having count_c >0 order by u.id limit 1 offset 0',[email,password])
        users = User.objects.filter(email=email, password=password)
        # user not found -> return error
        if not users.exists():
            return HttpResponse(json.dumps(constants.USER_NOT_FOUND), status=404, content_type="application/json")
        else:
            user = users[0]
            now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
            # if token has been expired, active new one
            if user.token == '' or user.tokenExpiredOn is None or user.tokenExpiredOn < now:
                user.token = uuid.uuid4().__str__()
                user.tokenExpiredOn = datetime.now() + timedelta(hours=24)
                user.save()
            # generate json response
            responseData = {}
            responseData['email'] = user.email
            responseData['password'] = user.password
            responseData['token'] = user.token
            responseData['fullName'] = user.fullName
            responseData['tokenExpiredOn'] = time.mktime(user.tokenExpiredOn.timetuple())

            return HttpResponse(json.dumps(responseData), status=200, content_type="application/json")
