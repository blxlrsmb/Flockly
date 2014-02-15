from flask import session, Response, request
from flockly import app, basefunc
from facebook import GraphAPI
import flockly.authpage
import flockly.blockly
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


@app.route('/upload_blockly', methods=['POST'])
@basefunc.auth_required
def upload_blockly():
    id = None
    if 'id' in request.form:
        id = request.form['id']
    a_blockly = None
    if id:
        a_blockly = list(flockly.blockly.Blockly.objects(id=id, userid=session['uid']))
        if a_blockly:
            a_blockly = a_blockly[0]
        else:
            return Response('', status=404)
    else:
        a_blockly = flockly.blockly.Blockly()
        a_blockly['userid'] = session['uid']

    a_blockly['content'] = request.form['content']
    a_blockly['name'] = request.form['name']

    a_blockly.save()
    return str(a_blockly.id)



@app.route('/get_blocklies_list')
@basefunc.auth_required
@basefunc.tojson
def get_blockly_list():
    blocklies = []
    for i in flockly.blockly.Blockly.objects(userid=session['uid']):
        blocklies.append({'id': str(i.id), 'name': i.name})
    return blocklies


@app.route('/get_blockly')
@basefunc.auth_required
@basefunc.tojson
def get_blockly():
    a_blockly = list(flockly.blockly.Blockly.objects(id=request.args.get('id', ''), userid=session['uid']))
    if a_blockly:
        a_blockly = a_blockly[0]
        return {
                'id': str(a_blockly.id),
                'userid': a_blockly.userid,
                'content': a_blockly.content,
                'name': a_blockly.name
                }
    else:
        return Response('', status=404)


@app.route('/get_profile')
@basefunc.auth_required
@basefunc.tojson
def get_profile():
    token = flockly.authpage.get_user_access_token(session['uid'])
    graph = GraphAPI(token)
    profile = graph.get('/me?fields=id,name,picture&access_token=%s&' % (token))
    return profile
