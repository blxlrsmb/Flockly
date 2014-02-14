from flask import Flask
app = Flask(__name__)

from flockly import config
from flockly import basefunc

import flockly.helloworld
import flockly.authpage
import flockly.flocklyapi

import flockly.mongo

