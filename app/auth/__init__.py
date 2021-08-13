from flask import render_template
from flask.blueprints import Blueprint
auth = Blueprint('auth',__name__)

from . import views,forms