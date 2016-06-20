from django.db import models
import datetime


# Create your models here.
class Channel(models.Model):
    created_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    updated_date = models.DateTimeField(null=False, default=datetime.datetime.now())
    name = models.CharField(max_length=100)

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
    avatar_id  = models.CharField(null=True, blank=True, max_length=100)

    def __unicode__(self):
        return self.name

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
    avatar_id = models.CharField(null=True, blank=True, max_length=100)

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "document_tab"
