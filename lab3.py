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


@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
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