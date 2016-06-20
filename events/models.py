from django.db import models
import datetime


# Create your models here.
class Channel(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "channel_tab"


class User(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    fullName = models.CharField(db_column='full_name',max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100,null=True)
    isAdmin = models.BooleanField(db_column='is_admin',default=False)
    tokenExpiredOn = models.DateTimeField(db_column='token_expired_on', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "user_account_tab"


class Event(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    startDate = models.DateTimeField(db_column='start_date', null=False, default=datetime.datetime.now())
    endDate = models.DateTimeField(db_column='end_date', null=False, default=datetime.datetime.now())
    channel = models.ForeignKey(Channel, null=False)
    creator = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "event_tab"


class Participant(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "participant_tab"


class Like(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "like_tab"


class Comment(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    mainComment = models.ForeignKey('self', null=True, db_column='main_comment')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "comment_tab"


class Document(models.Model):
    createdDate = models.DateTimeField(db_column='created_date', null=False, default=datetime.datetime.now())
    updatedDate = models.DateTimeField(db_column='updated_date', null=False, default=datetime.datetime.now())
    user = models.ForeignKey(User, null=True)
    event = models.ForeignKey(Event, null=True)
    name = models.CharField(max_length=100, null=True)
    physicalId = models.CharField(db_column='physical_id',max_length=36)
    isMain = models.BooleanField(db_column='is_main',default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "document_tab"
