# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, url_for
# )
# from werkzeug.exceptions import abort

# from app.auth import login_required
# from app import get_db

# bp = Blueprint('blog', __name__)


from flask import Blueprint

blog = Blueprint('auth',__name__)

from . import views,forms