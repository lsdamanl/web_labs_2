from flask import Blueprint, render_template, request, redirect, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
import sqlite3
from os import path
lab6 = Blueprint('lab6', __name__)


def initialize_offices_table():
    offices = []
    for i in range(1, 11):
        offices.append({"number": i, "tenant": "", "price": 900 + i % 3})

    conn, cur = db_connect()
    db_close(conn, cur)



@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')
def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'shipilov_dmitriy_knowledge_base',
            user = 'shipilov_dmitriy_knowledge_base',
            password = '123'
        )
        cur = conn.cursor(cursor_factory = RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data.get('id')
    conn, cur = db_connect()

    try:
        if data['method'] == 'info':
            login = session.get('login', '')
            
            cur.execute('SELECT * FROM offices;')
            offices = cur.fetchall()

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute('SELECT SUM(price) AS total_rent FROM offices WHERE tenant = %s;', (login,))
            else:
                cur.execute('SELECT SUM(price) AS total_rent FROM offices WHERE tenant = ?;', (login,))
            total_rent = cur.fetchone()['total_rent'] or 0

            result = {
                'offices': [
                    {
                        'number': office['number'],
                        'tenant': office['tenant'],
                        'price': office['price'],
                    }
                    for office in offices
                ],
                'total_rent': total_rent,
            }
            return {'jsonrpc': '2.0', 'result': result, 'id': id}

        login = session.get('login')
        if not login:
            return {
                'jsonrpc': '2.0',
                'error': {'code': 1, 'message': 'Unauthorized'},
                'id': id,
            }

        if data['method'] == 'booking':
            office_number = data['params']

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute('SELECT * FROM offices WHERE number = %s;', (office_number,))
            else:
                cur.execute('SELECT * FROM offices WHERE number = ?;', (office_number,))
            
            office = cur.fetchone()

            if not office:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 5, 'message': 'Office not found'},
                    'id': id,
                }

            if office['tenant']:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 2, 'message': 'Already booked'},
                    'id': id,
                }

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute('UPDATE offices SET tenant = %s WHERE number = %s;', (login, office_number))
            else:
                cur.execute('UPDATE offices SET tenant = ? WHERE number = ?;', (login, office_number))
            
            return {
                'jsonrpc': '2.0',
                'result': f'Office {office_number} booked',
                'id': id,
            }

        if data['method'] == 'cancellation':
            office_number = data['params']

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute('SELECT * FROM offices WHERE number = %s;', (office_number,))
            else:
                cur.execute('SELECT * FROM offices WHERE number = ?;', (office_number,))
            
            office = cur.fetchone()

            if not office:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 5, 'message': 'Office not found'},
                    'id': id,
                }

            if not office['tenant']:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 3, 'message': 'Office not booked'},
                    'id': id,
                }

            if office['tenant'] != login:
                return {
                    'jsonrpc': '2.0',
                    'error': {'code': 4, 'message': 'You cannot cancel someone else booking'},
                    'id': id,
                }

            if current_app.config['DB_TYPE'] == 'postgres':
                cur.execute('UPDATE offices SET tenant = NULL WHERE number = %s;', (office_number,))
            else:
                cur.execute('UPDATE offices SET tenant = NULL WHERE number = ?;', (office_number,))
            
            return {
                'jsonrpc': '2.0',
                'result': f'Office {office_number} booking canceled',
                'id': id,
            }

        return {
            'jsonrpc': '2.0',
            'error': {'code': -32601, 'message': 'Method not found'},
            'id': id,
        }

    except Exception as e:
        return {
            'jsonrpc': '2.0',
            'error': {'code': -32000, 'message': f'Internal error: {str(e)}'},
            'id': id,
        }

    finally:
        db_close(conn, cur)
