# define the custom middleware for authentication
import json

from django.http import HttpResponse

from events.models import User
from events import constants
from datetime import datetime


class AuthenticationMiddleware(object):
    def process_request(self, request):
        # if login or signup --> pass through the url
        if 'signup' in request.get_full_path() \
                or 'login' in request.get_full_path():
            return None
        token = None
        if request.method == 'GET':
            if 'token' in request.GET:
                token = request.GET["token"]
        else:
            if 'token' in request.POST:
                token = request.POST['token']
        if (token == None):
            return HttpResponse(json.dumps({'error': constants.TOKEN_NOT_FOUND_OR_EXPIRED}), status=403,
                                content_type="application/json")
        else:
            users = User.objects.filter(token=token)
            if not users.exists():
                return HttpResponse(json.dumps({'error': constants.TOKEN_NOT_FOUND_OR_EXPIRED}), status=403,
                                    content_type="application/json")
            else:
                # if token expired, not pass
                if users[0].tokenExpiredOn < datetime.utcnow():
                    return HttpResponse(json.dumps({'error': constants.TOKEN_NOT_FOUND_OR_EXPIRED}), status=403,
                                        content_type="application/json")

    def process_template_response(self, request, response):
        return response
