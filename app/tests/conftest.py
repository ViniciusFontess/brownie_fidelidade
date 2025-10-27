import os
import sys

# Ajustar sys.path para que o pacote interno `app/` seja facilmente importável
HERE = os.path.dirname(__file__)
# inserir a pasta que contém o pacote `app` (um nível acima dos testes)
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)