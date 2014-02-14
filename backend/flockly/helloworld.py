from flockly import app

@app.route('/hello-world')
def hello_world():
    return 'Hello World'
