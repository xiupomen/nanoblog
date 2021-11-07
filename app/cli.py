import os
import click


def register(app):
    @app.cli.group()
    def nanoblog():
        """Nanoblog commands."""
        pass

    @nanoblog.command()
    @click.argument('msg')
    def init(msg):
        """Initialize message."""
        print(msg)
        # if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        #     raise RuntimeError('extract command failed')
        # if os.system(
        #         'pybabel init -i messages.pot -d app/translations -l ' + lang):
        #     raise RuntimeError('init command failed')
        # os.remove('messages.pot')

    @nanoblog.command()
    def update():
        """Update all."""
        print('update')
        # if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        #     raise RuntimeError('extract command failed')
        # if os.system('pybabel update -i messages.pot -d app/translations'):
        #     raise RuntimeError('update command failed')
        # os.remove('messages.pot')

    @nanoblog.command()
    def compile():
        """Compile all."""
        print('compile')
        # if os.system('pybabel compile -d app/translations'):
        #     raise RuntimeError('compile command failed')