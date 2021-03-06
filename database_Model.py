from google.appengine.ext import ndb


class User(ndb.Model):
    userMail = ndb.StringProperty()
    nickname = ndb.StringProperty()
    lastSignInTime = ndb.DateTimeProperty(auto_now=True, indexed=False)
    signUpDate = ndb.DateTimeProperty(auto_now_add=True, indexed=False)


class Group(ndb.Model):
    groupName = ndb.StringProperty()
    makeUserNickname = ndb.StringProperty()


class GroupMap(ndb.Model):
    userMail = ndb.StringProperty()
    groupId = ndb.IntegerProperty()


class Device(ndb.Model):
    deviceKey = ndb.StringProperty()
    deviceName = ndb.StringProperty()
    googleCalendarId = ndb.StringProperty()
    registeredGroupId = ndb.IntegerProperty()
    registeredUser = ndb.StringProperty()
    registeredTime = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
    accessTime = ndb.DateTimeProperty(auto_now=True, indexed=False)
    # mappedContentId = ndb.IntegerProperty()


class Content(ndb.Model):
    contentName = ndb.StringProperty()
    googleCalendarId = ndb.StringProperty()
    madeGroupId = ndb.StringProperty()
    madeUserId = ndb.StringProperty()
    madeTime = ndb.DateTimeProperty(auto_now=True)