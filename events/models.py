from django.db import models
import datetime
import time

# Create your models here.
class Channel(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    name = models.CharField(max_length=100)

    def to_json(self):
        result  = {}
        result['id'] = self.id
        result['name'] = self.name
        result['created_date'] = time.mktime(self.created_date.timetuple())
        result['updated_date'] = time.mktime(self.updated_date.timetuple())
        return result

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "channel_tab"


class User(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100,null=True)
    is_admin = models.BooleanField(default=False)
    token_expired_on = models.DateTimeField(null=True, blank=True)
    avatar_id = models.FileField(upload_to='documents/%Y/%m/%d')

    def to_json(self):
        result = {}
        result['email'] = self.email
        result['password'] = self.password
        result['token'] = self.token
        result['full_name'] = self.full_name
        result['token_expired_on'] = time.mktime(self.token_expired_on.timetuple())
        result['is_admin'] = self.is_admin
        result['avatar_id'] = self.avatar_id.__str__()
        return result

    def __unicode__(self):
        return self.full_name

    class Meta:
        db_table = "user_account_tab"


class Event(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    start_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    end_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    channel = models.ForeignKey(Channel, null=False)
    creator = models.ForeignKey(User)
    avatar_id = models.FileField(upload_to='documents/%Y/%m/%d')

    def to_json(self):
        result = {}
        result['id'] = self.id
        result['title'] = self.title
        result['start_date'] = time.mktime(self.start_date.timetuple())
        result['end_date'] = time.mktime(self.end_date.timetuple())
        result['created_date'] = time.mktime(self.created_date.timetuple())
        result['description'] = self.description
        result['avatar_id'] = self.avatar_id.__str__()
        return result

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "event_tab"


class Participant(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "participant_tab"


class Like(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "like_tab"


class Comment(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    main_comment = models.ForeignKey('self', null=True, db_column='main_comment')
    content = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "comment_tab"


class Document(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User, null=True)
    event = models.ForeignKey(Event, null=True)
    name = models.CharField(max_length=100, null=True)
    physical_id = models.CharField(max_length=36)
    is_main = models.BooleanField(default=False)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "document_tab"
