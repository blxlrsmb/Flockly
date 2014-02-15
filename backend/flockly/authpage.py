from flockly import app
from flockly import config
from flockly.user import User
from facebook import FacebookAPI, FacebookClientError, GraphAPI
from flask import redirect, request, session
import time



@app.route('/auth')
def auth():
    f = FacebookAPI(config.API_KEY, config.API_SECRET, config.REDIRECT_URL)
    auth_url = f.get_auth_url(scope=[
        "publish_stream", "read_stream", "status_update", "user_friends", "friends_birthday", "friends_hometown", "friends_location"
        ])
    return redirect(auth_url)

@app.route('/auth_redirect')
def auth_redirect():
    f = FacebookAPI(config.API_KEY, config.API_SECRET, config.REDIRECT_URL)
    try:
        access_token = f.get_access_token(request.args.get('code', ''))
        graph = GraphAPI(access_token['access_token'])
        id = graph.get('me')['id']
        save_user(id, access_token['access_token'], int(int(access_token['expires']) + time.time() - 3600))
        session['uid'] = id
        return redirect('/')
    except FacebookClientError as e:
        return 'Authorization Failed:' + str(e)

def save_user(userid, access_token, access_token_expires):
    User(userid=userid, access_token=access_token,
         access_token_expires=access_token_expires).save()

def get_user_access_token(userid):
    return User.objects(userid=userid)[0].get_access_token()
