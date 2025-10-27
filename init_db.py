#!/usr/bin/env python3
import sys
import os

# Colocar o diretório `app/` (o pacote Flask) no início de sys.path
HERE = os.path.dirname(__file__)
INNER_APP = os.path.join(HERE, 'app')
if INNER_APP not in sys.path:
    sys.path.insert(0, INNER_APP)

try:
    from app import create_app
    from app.db import init_db
except Exception:
    # fallback: importar pelo submódulo
    from app.app import create_app
    from app.db import init_db


def main():
    app = create_app()
    init_db(app)
    print('Banco inicializado em', app.instance_path)


if __name__ == '__main__':
    main()
