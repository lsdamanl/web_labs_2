from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
 

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers_html(flower_id):
    if flower_id >= len(flower_list):
        return '''
<!doctype html>
<html>
    <body>
        <h1>Ошибка</h1>
        <p>Такого цветка нет, братик</p>
        <a href="/lab2/all_flowers">Список всех цветов</a>
    </body>
</html>
        ''', 404
    else:
        flower = flower_list[flower_id]
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Цветок: {flower}</h1>
        <a href="/lab2/all_flowers">Список всех цветов</a>
    </body>
</html>
        '''


@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.lab2end(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок </h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''


@lab2.route('/lab2/example')
def example():
    name = 'Дмитрий Шипилов'
    group = 'ФБИ-24'
    number_course = '3 курс'
    number_lab = '2'
    fruits = [
        {'name' :'яблоки', 'price': 100},
        {'name' :'груши', 'price': 120},
        {'name' :'апельсины', 'price': 80},
        {'name' :'мандарины', 'price': 95},
        {'name' :'манго', 'price': 321}
        ]
    return render_template('example.html', name=name, group=group, number_course=number_course, number_lab=number_lab, fruits=fruits)
   

@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)


@lab2.route('/lab2/add_flower/', defaults={'name': None})
def add_flower_with_default(name):
    if not name:
        return "Вы не задали имя цветка", 400
    return add_flower(name)


@lab2.route('/lab2/all_flowers')
def all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список всех цветов</h1>
        <p>Количество цветов: {len(flower_list)}</p>
        <ul>
            {''.join([f'<li>{flower}</li>' for flower in flower_list])}
        </ul>
        <a href="/lab2/clear_flowers">Очистить список цветов</a>
    </body>
</html>
'''


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''
<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен</h1>
        <a href="/lab2/all_flowers">Список всех цветов</a>
    </body>
</html>
'''


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Расчёт с параметрами:</h1>
        <p>{a} + {b} = {a + b}</p>
        <p>{a} - {b} = {a - b}</p>
        <p>{a} * {b} = {a * b}</p>
        <p>{a} / {b} = {a / b if b != 0 else "деление на ноль невозможно"}</p>
        <p>{a}<sup>{b}</sup> = {a ** b}</p>
    </body>
</html>
    '''


@lab2.route('/lab2/calc/')
def calc_default_redirect():
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>')
def calc_with_redirect(a):
    return redirect(url_for('calc', a=a, b=1))


@lab2.route('/lab2/books')
def show_books():
    books = [
        {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
        {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1225},
        {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328},
        {"author": "Габриэль Гарсия Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 417},
        {"author": "Даниэль Дефо", "title": "Робинзон Крузо", "genre": "Приключения", "pages": 320},
        {"author": "Джон Рональд Руэл Толкин", "title": "Властелин колец", "genre": "Фэнтези", "pages": 1137},
        {"author": "Артур Конан Дойл", "title": "Приключения Шерлока Холмса", "genre": "Детектив", "pages": 305},
        {"author": "Агата Кристи", "title": "Убийство в Восточном экспрессе", "genre": "Детектив", "pages": 288},
        {"author": "Александр Дюма", "title": "Граф Монте-Кристо", "genre": "Роман", "pages": 1243},
        {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 480},
    ]
    return render_template('books.html', books=books)


@lab2.route('/lab2/cars')
def show_cars():
    cars = [
        {"name": "BMW", "description": "Немецкий производитель автомобилей, известных своей динамичностью и качеством.", "image": "bmw.jpg"},
        {"name": "Mercedes", "description": "Люксовый бренд, символизирующий стиль, комфорт и технологичность.", "image": "mercedes.webp"},
        {"name": "Audi", "description": "Известный немецкий бренд, выпускающий премиальные автомобили с передовыми технологиями.", "image": "audi.jpg"},
        {"name": "Toyota", "description": "Японская компания, производящая надежные автомобили для широкого круга потребителей.", "image": "toyota.png"},
        {"name": "Tesla", "description": "Американская компания, выпускающая инновационные электромобили с автопилотом.", "image": "tesla.webp"},
    ]
    cars_html = '''
    <!doctype html>
    <html>
        <head>
            <style>
                .car-container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-around;
                }
                .car-item {
                    width: 30%;
                    text-align: center;
                    margin-bottom: 20px;
                }
                .car-item img {
                    width: 100%;
                    height: auto;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                }
                .car-item h2 {
                    font-size: 24px;  
                }
                .car-item p {
                    font-size: 20px;  
                }
            </style>
        </head>
        <body>
            <h1 style="text-align:center;">Список автомобилей</h1>
            <div class="car-container">
    '''
    for car in cars:
        cars_html += f'''
        <div class="car-item">
            <img src="/static/{car['image']}" alt="{car['name']}">
            <h2>{car['name']}</h2>
            <p>{car['description']}</p>
        </div>
        '''
    cars_html += '''
            </div>
        </body>
    </html>
    '''
    return cars_html