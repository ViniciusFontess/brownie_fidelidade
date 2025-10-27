import tempfile
import sqlite3
import os
import sys
import pytest

# garantir que o pacote interno `app/` seja importado (evita ambiguidade com a pasta externa)
HERE = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, '..'))
INNER_APP = os.path.join(PROJECT_ROOT, 'app')
if INNER_APP not in sys.path:
    sys.path.insert(0, INNER_APP)

from app import create_app
from app.db import init_db


@pytest.fixture
def client(tmp_path):
    db_file = tmp_path / "test_brownies.sqlite"
    app = create_app()
    app.config['TESTING'] = True
    app.config['DATABASE'] = str(db_file)
    init_db(app)
    with app.test_client() as c:
        yield c


def test_db_created(tmp_path):
    db_file = tmp_path / "test_brownies.sqlite"
    app = create_app()
    app.config['DATABASE'] = str(db_file)
    init_db(app)
    con = sqlite3.connect(str(db_file))
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    con.close()
    assert 'purchases' in tables


def test_post_and_admin_counts(client):
    r = client.post('/api/purchases', data={'cpf': '99988877766', 'quantity': '3'})
    assert r.status_code == 200
    r = client.post('/api/purchases', data={'cpf': '99988877766', 'quantity': '8'})
    assert r.status_code == 200
    r = client.get('/admin')
    assert r.status_code == 200
    html = r.get_data(as_text=True)
    assert '99988877766' in html
    assert '11' in html
    assert '1' in html
