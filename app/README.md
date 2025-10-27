Brownie Fidelidade
===================

Sistema simples de fidelidade para vendas de brownies.

Como funciona
- Cliente escaneia o QR Code que aponta para `/scan`.
- Preenche nome, CPF e quantidade comprada.
- O sistema registra a compra em SQLite.
- O admin acessa `/admin` para ver o total de brownies por CPF e quantos "prêmios" (1 a cada 10 unidades) cada pessoa tem.

Rodando localmente

1. Crie e ative um virtualenv (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Inicialize o banco:

```bash
python -m app.app init-db
```

4. Rode o servidor:

```bash
python -m app.app run
```

Abra http://127.0.0.1:5000/scan para testar. A rota `/admin` mostra o painel de controle.
