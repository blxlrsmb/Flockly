#!/usr/bin/env python2.7
from flockly import app
import random
rand = random.SystemRandom()
app.secret_key = ''.join([chr(rand.randint(0, 255)) for i in range(100)])
app.run(debug=True)
