from flask import (
    Blueprint, current_app, g, render_template, request, redirect, url_for, send_file
)
import sqlite3
from .db import get_db
import io

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return redirect(url_for('main.scan'))


@bp.route('/scan', methods=['GET'])
def scan():
    return render_template('scan.html')


@bp.route('/api/purchases', methods=['POST'])
def api_purchases():
    data = request.form or request.get_json() or {}
    cpf = data.get('cpf')
    try:
        qty = int(data.get('quantity', 0))
    except (TypeError, ValueError):
        qty = 0

    if not cpf or qty <= 0:
        return {'error': 'cpf e quantity são obrigatórios e quantity > 0'}, 400

    db = get_db()
    cur = db.cursor()
    # armazenamos apenas cpf e quantity; o campo name existe no DB legado mas não é usado
    cur.execute(
        'INSERT INTO purchases (name, cpf, quantity) VALUES (?, ?, ?)',
        (None, cpf, qty)
    )
    db.commit()
    return {'status': 'ok'}


@bp.route('/admin')
def admin():
    db = get_db()
    cur = db.cursor()
    # Agrupar por CPF apenas para somar todas as compras do mesmo cliente
    cur.execute('SELECT cpf, SUM(quantity) as total FROM purchases GROUP BY cpf ORDER BY total DESC')
    rows = cur.fetchall()
    results = []
    for r in rows:
        cpf, total = r
        prizes = total // 10
        results.append({'cpf': cpf, 'total': total, 'prizes': prizes})
    return render_template('admin.html', results=results)


@bp.route('/qr.png')
def qr_png():
    try:
        import qrcode
    except Exception:
        return ('qrcode library não instalada', 501)
    qr_io = io.BytesIO()
    img = qrcode.make(url_for('main.scan', _external=True))
    img.save(qr_io, format='PNG')
    qr_io.seek(0)
    return send_file(qr_io, mimetype='image/png')
