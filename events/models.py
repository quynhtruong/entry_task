from django.db import models
import datetime


# Create your models here.
class Channel(models.Model):
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "channel_tab"


class User(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    token = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False,name='is_admin')
    tokenExpiredOn = models.DateTimeField('token_expired_on', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "user_account_tab"


class Event(models.Model):
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    startDate = models.DateTimeField('start_date', null=False, default=datetime.datetime.now())
    endDate = models.DateTimeField('end_date', null=False, default=datetime.datetime.now())
    channel = models.ForeignKey(Channel, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "event_tab"


class Participant(models.Model):
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "participant_tab"


class Like(models.Model):
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "like_tab"


class Comment(models.Model):
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    mainComment = models.ForeignKey('self', null=True, name='main_comment')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "comment_tab"


class Document(models.Model):
    createdDate = models.DateTimeField('created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField('updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User, null=True)
    event = models.ForeignKey(Event, null=True)
    name = models.CharField(max_length=100, null=True)
    physicalId = models.CharField(max_length=36)
    isMain = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "document_tab"
