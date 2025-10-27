import os
from flask import Flask
from .db import init_db, close_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # definir caminho consistente para o DB dentro da pasta `app/instance`
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    instance_dir = os.path.join(base_dir, 'instance')
    os.makedirs(instance_dir, exist_ok=True)
    db_path = os.path.join(instance_dir, 'brownies.sqlite')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=db_path,
    )

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Close DB connection on teardown
    app.teardown_appcontext(close_db)

    from . import app as app_module
    app.register_blueprint(app_module.bp)

    @app.cli.command('init-db')
    def init_db_command():
        init_db(app)
        print('Banco inicializado.')

    return app
