# coding: utf-8
import mongo
import sys
from user import User
from blockly import Blockly
from facebook import *
from dateutil import parser
import time
import datetime
import json
import requests

class FBUser:
    name = None # name
    id = None # id
    # city = None # location.name
    # sex = None # gender
    # birthday = None # birthday mm/dd/yyyy
    def __str__(self):
        return self.name.encode('utf-8')
    def __unicode__(self):
        return self.name
    def __repr__(self):
        return str(self)
    def __getattr__(self, name):
        if hasattr(self, name):
            return self.__dict__[name]
        user_complete = getUserinfo(self.id)
        self.city = user_complete.city
        self.sex = user_complete.sex
        self.has_birthday = user_complete.has_birthday
        self.birthday = user_complete.birthday
        return getattr(self, name)



class FBStatus:
    id = None
    author = None
    content = None
    time = None
    location = None
    def __str__(self):
        return self.content.encode('utf-8')
    def __unicode__(self):
        return self.content
    def __repr__(self):
        return str(self)

FBUsers = {}


UID = sys.argv[1]
U = User.objects(userid=UID)[0]
access_token = U.access_token

BID = sys.argv[2]
B = Blockly.objects(id=BID)[0]

def updateStatus(message):
    graph = GraphAPI(access_token)
    graph.post('/me/feed', params={'message': message})


def commentStatus(status, comment):
    graph = GraphAPI(access_token)
    graph.post('/%s/comments' % (status.id), params={'message': comment})


def getAllStatus():
    graph = GraphAPI(access_token)
    statuses = []
    for i in graph.get('me/home?since=%s&access_token=%s&' % (B.lastexecution, access_token))['data']:
        status = FBStatus()
        status.id = i['id']
        status.author = FBUser()
        status.author.id = i['from']['id']
        status.author.name = i['from']['name']
        if 'message' in i:
            status.content = i['message']
        else:
            status.content = ''
        status.time = datetime.datetime.fromtimestamp(
                time.mktime(
                    parser.parse(i['created_time']).utctimetuple()
                    )
                )
        if 'place' in i and 'location' in i['place'] and 'city' in i['place']['location']:
            status.location = i['place']['location']['city']
        else:
            status.location = ''
        statuses.append(status)
    return statuses

def getUserinfo(uid):
    graph = GraphAPI(access_token)
    user = graph.get('/' + uid)
    rt_user = FBUser()
    rt_user.id = user['id']
    rt_user.name = user['name']
    if 'location' in user and 'name' in user['location']:
        rt_user.city = user['location']['name']
    else:
        rt_user.city = ""
    if 'gender' in user:
        rt_user.sex = user['gender']
    else:
        rt_user.sex = ""
    if 'birthday' in user:
        rt_user.birthday = parser.parse(user['birthday'])
        rt_user.has_birthday = True
    else:
        rt_user.has_birthday = False
        rt_user.birthday = None
    return rt_user

def getFriends():
    graph = GraphAPI(access_token)
    friends = []
    res = graph.get('/me/friends')
    while res['data']:
        for i in res['data']:
            fri = FBUser()
            fri.id = i['id']
            fri.name = i['name']
            friends.append(fri)
        if 'paging' in res and 'next' in res['paging']:
            res = json.loads(requests.get(res['paging']['next']).text)
    return friends


