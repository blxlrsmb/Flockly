from flask import Flask
app = Flask(__name__)

from flockly import config

import flockly.helloworld
import flockly.authpage

