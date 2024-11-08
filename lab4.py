from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods= ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)

    if x2 == 0:
        return render_template('lab4/div.html', error='Делить на ноль нельзя! Пожалуйста, введите другое значение.')

    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/add-form')
def add_form():
    return render_template('lab4/add-form.html')


@lab4.route('/lab4/add', methods=['POST'])
def add():
    x1 = request.form.get('x1') or '0'
    x2 = request.form.get('x2') or '0'
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2
    return render_template('lab4/add.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')


@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1 = request.form.get('x1') or '1'
    x2 = request.form.get('x2') or '1'
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2
    return render_template('lab4/mul.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')


@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')


@lab4.route('/lab4/pow', methods=['POST'])
def pow():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/pow.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x1 == 0 and x2 == 0:
        return render_template('lab4/pow.html', error='0 в степени 0 не определено!')
    result = x1 ** x2
    return render_template('lab4/pow.html', x1=x1, x2=x2, result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut' and tree_count > 0:
        tree_count -= 1
    elif operation == 'plant' and tree_count < 10:
        tree_count += 1

    return redirect('/lab4/tree')  


users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Иванов', 'gender': 'мужской'},
    {'login': 'bob', 'password': '555', 'name': 'Боб Смит', 'gender': 'мужской'},
    {'login': 'altushka', 'password': '12345', 'name': 'Катя Петрова', 'gender': 'женский'},
    {'login': 'baltika7', 'password': '321', 'name': 'Иван Сергеев', 'gender': 'мужской'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            user = next((u for u in users if u['login'] == session['login']), None)
            if user:
                name = user['name']
                return render_template('lab4/login.html', authorized=True, name=name)
        return render_template('lab4/login.html', authorized=False, login='')

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    user = next((u for u in users if u['login'] == login and u['password'] == password), None)
    if user:
        session['login'] = login
        return redirect('/lab4/login')

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'POST':
        temperature = request.form.get('temperature')
        
        if temperature == '':
            error = 'Ошибка: не задана температура'
            return render_template('lab4/fridge.html', error=error)
        
        try:
            temperature = int(temperature)
        except ValueError:
            error = 'Ошибка: введите числовое значение'
            return render_template('lab4/fridge.html', error=error)
        
        if temperature < -12:
            error = 'Не удалось установить температуру — слишком низкое значение'
            return render_template('lab4/fridge.html', error=error)
        elif temperature > -1:
            error = 'Не удалось установить температуру — слишком высокое значение'
            return render_template('lab4/fridge.html', error=error)
        
        snowflakes = 3 if -12 <= temperature <= -9 else 2 if -8 <= temperature <= -5 else 1
        message = f'Установлена температура: {temperature}°С'
        return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)
    
    return render_template('lab4/fridge.html')