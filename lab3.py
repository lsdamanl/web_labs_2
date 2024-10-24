from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'Anonymous')
    age = request.cookies.get('age', '?')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20', max_age=5)
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    errors1 = {}
    if age == '':
        errors['age'] = 'Заполните поле!'


    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара - на 10
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

 
    resp = make_response(render_template('lab3/pay.html', price=price))
    resp.set_cookie('price', str(price))
    return resp


@lab3.route('/lab3/success')
def success():
    price = request.cookies.get('price') 
    return render_template('lab3/success.html', price=price)



@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    bgcolor = request.args.get('bgcolor')
    font_size = request.args.get('font_size')
    bold = request.args.get('bold')
    if color or bgcolor or font_size or bold:
        resp = make_response(redirect('/lab3/settings'))

        if color:
            resp.set_cookie('color', color)
        if bgcolor:
            resp.set_cookie('bgcolor', bgcolor)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if bold:
            resp.set_cookie('bold', bold)
        else:
            resp.set_cookie('bold', '', expires=0) 
        return resp

    color = request.cookies.get('color')
    bgcolor = request.cookies.get('bgcolor')
    font_size = request.cookies.get('font_size')
    bold = request.cookies.get('bold')
    resp = make_response(render_template('lab3/settings.html', color=color, bgcolor=bgcolor, font_size=font_size, bold=bold))
    return resp


@lab3.route('/lab3/ticket', methods=['get', 'post'])
def ticket():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        date = request.form.get('date')
        berth = request.form.get('berth')
        bedding = 'bedding' in request.form
        luggage = 'luggage' in request.form
        insurance = 'insurance' in request.form

        if age < 18:
            ticket_type = 'Детский билет'
            price = 700
        else:
            ticket_type = 'Взрослый билет'
            price = 1000

        if berth in ['нижняя', 'нижняя боковая']:
            price += 100


        if bedding:
            price += 75
        if luggage:
            price += 250
        if insurance:
            price += 150

        return render_template('lab3/ticket.html', name=name, age=age, departure=departure,
                               destination=destination, date=date, berth=berth, bedding=bedding,
                               luggage=luggage, insurance=insurance, ticket_type=ticket_type, price=price)
    
    return render_template('lab3/ticket_form.html')


products = [
    {"name": "NVIDIA GeForce RTX 4090", "price": 250000, "memory": "24 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce RTX 4080", "price": 130000, "memory": "16 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce RTX 4070 Ti SUPER", "price": 102000, "memory": "12 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce RTX 4070", "price": 65000, "memory": "12 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce RTX 4060 Ti", "price": 60000, "memory": "8 GB", "brand": "NVIDIA"},
    {"name": "AMD Radeon RX 7900 XTX", "price": 140000, "memory": "24 GB", "brand": "AMD"},
    {"name": "AMD Radeon RX 7900 XT", "price": 96000, "memory": "20 GB", "brand": "AMD"},
    {"name": "AMD Radeon RX 6800 XT", "price": 63000, "memory": "16 GB", "brand": "AMD"},
    {"name": "AMD Radeon RX 6800", "price": 55000, "memory": "16 GB", "brand": "AMD"},
    {"name": "NVIDIA GeForce GTX 1660 Super", "price": 23000, "memory": "6 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce GTX 1650", "price": 16000, "memory": "4 GB", "brand": "NVIDIA"},
    {"name": "AMD Radeon RX 6600 XT", "price": 70000, "memory": "8 GB", "brand": "AMD"},
    {"name": "AMD Radeon RX 6500 XT", "price": 18000, "memory": "4 GB", "brand": "AMD"},
    {"name": "NVIDIA GeForce RTX 3060 Ti", "price": 37000, "memory": "8 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce RTX 3060", "price": 33000, "memory": "12 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce RTX 2060", "price": 20000, "memory": "4 GB", "brand": "NVIDIA"},
    {"name": "AMD Radeon RX 5700 XT", "price": 60000, "memory": "8 GB", "brand": "AMD"},
    {"name": "AMD Radeon RX 580", "price": 9000, "memory": "8 GB", "brand": "AMD"},
    {"name": "NVIDIA GeForce GT 1030", "price": 8000, "memory": "2 GB", "brand": "NVIDIA"},
    {"name": "NVIDIA GeForce GTX 1050 Ti", "price": 6000, "memory": "4 GB", "brand": "NVIDIA"},
]

@lab3.route('/lab3/search_form')
def search_form():
    min_price = request.args.get('min_price') or request.cookies.get('min_price', '0')
    max_price = request.args.get('max_price') or request.cookies.get('max_price', '250000')

    return render_template('lab3/search_form.html', min_price=min_price, max_price=max_price)


@lab3.route('/lab3/search', methods=['get'])
def search():
    min_price = request.args.get('min_price', '0')
    max_price = request.args.get('max_price', '250000')

    min_price = int(min_price)
    max_price = int(max_price)
    filtered_products = [product for product in products if min_price <= product["price"] <= max_price]

    resp = make_response(render_template('lab3/results.html', products=filtered_products, min_price=min_price, max_price=max_price))
    resp.set_cookie('min_price', str(min_price))
    resp.set_cookie('max_price', str(max_price))

    return resp

    