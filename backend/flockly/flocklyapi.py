from flask import session
from flockly import app, basefunc
from facebook import GraphAPI
import flockly.authpage
import requests
import json


@app.route('/get_friends')
@basefunc.auth_required
@basefunc.tojson
def get_friends():
    token = flockly.authpage.get_user_access_token(session['uid'])
    graph = GraphAPI(token)
    friends = []
    res = graph.get('/me/friends')
    while res['data']:
        friends = friends + res['data']
        if 'paging' in res and 'next' in res['paging']:
            res = json.loads(requests.get(res['paging']['next']).text)
    return friends

