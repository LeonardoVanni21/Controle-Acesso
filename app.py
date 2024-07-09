from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from psycopg2 import sql

app = Flask(__name__)
app.secret_key = 'secretKey123'

conn = psycopg2.connect(
    dbname="BaseControleAcesso",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)


def get_user_permissions(user_id):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT p.name 
            FROM permissions p
            JOIN user_permissions up ON p.id = up.permission_id
            WHERE up.user_id = %s
        """, (user_id,))
        return [row[0] for row in cur.fetchall()]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()

            if user:
                session['user_id'] = user[0]
                return redirect(url_for('dashboard'))
            else:
                return "Dados Incorretos", 403

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    permissions = get_user_permissions(user_id)

    return render_template('dashboard.html', permissions=permissions)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/tela_admin')
def tela_admin():
    return render_template('tela_admin.html')

@app.route('/tela_comum')
def tela_comum():
    return render_template('tela_comum.html')


if __name__ == '__main__':
    app.run(debug=True)