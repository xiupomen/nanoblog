from app import create_app, db, cli
from app.models import User, Post
from pywebio.platform.flask import webio_view

from tools import bmi, bkapp

app = create_app()
cli.register(app)

app.add_url_rule('/tools/bmi', 'bmi', webio_view(bmi),
            methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/tools/bokeh', 'bokeh', webio_view(bkapp),
            methods=['GET', 'POST', 'OPTIONS'])


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


