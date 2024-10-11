from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
        </nav>

        <footer>
            &copy; Шипилов Дмитрий Андреевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Шипилов Дмитрий Андреевич, лабораторная работа 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h3>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</h3>

        <h3>Реализованные роуты:</h3>
        <ul>
            <li><a href="/lab1/student">О студенте</a></li>
            <li><a href="/lab1/python">О языке Python</a></li>
            <li><a href="/lab1/oak">О дубе</a></li>
            <li><a href="/lab1/Mnogoznaal">О Mnogoznaal</a></li>
        </ul>

        <nav>
            <a href="/menu">Меню</a>
        </nav>

        <footer>
            &copy; Шипилов Дмитрий Андреевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''
@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Дуб</title>
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>О студенте</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Шипилов Дмитрий Андреевич</h1>
        <h2>Группа ФБИ-24, 3 курс</h2>
        <img src="''' + url_for('static', filename='nstu.png') + '''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python_info():
    return '''
<!doctype html>
<html>
    <head>
        <title>О языке Python</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Python</h1>
        <p>Python — это высокоуровневый язык программирования, отличающийся эффективностью, простотой и универсальностью использования.
        Он широко применяется в разработке веб-приложений и прикладного программного обеспечения, а также в машинном
        обучении и обработке больших данных. За счет простого и интуитивно понятного синтаксиса является одним из распространенных языков для обучения программированию. </p>

        <p>Python активно используется в таких областях, как веб-разработка, анализ данных, машинное обучение и автоматизация. 
        Благодаря простому синтаксису и большому количеству библиотек, Python стал одним из самых популярных языков программирования.</p>

        <img src="''' + url_for('static', filename='python.png') + '''">

    </body>
</html>
'''
@app.route("/lab1/Mnogoznaal")
def custom():
    return '''
<!doctype html>
<html>
    <head>
        <title>Mnogoznaal</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Mnogoznaal</h1>
        <p>Молодой российский рэпер и хип-хоп-исполнитель Mnogoznaal является представителем новой школы. 
        Слушателей по всей России парень завоевал глубокими текстами, спокойным необычным флоу (скорость читки) и качественным звучанием песен.</p>

        <p>Настоящее имя рэпера, выступающего под псевдонимом Mnogoznaal, - Максим Лазин.
        Мальчик родился в Печоре Республики Коми летом 1993 года. Этот город располагается
        между тайгой и тундрой, там суровый климат с преобладанием зимы. Уже будучи
        взрослым, Максим рассказывал: чтобы добраться до Москвы, на дорогу приходилось тратить очень много времени.</p>
        <p> Серьезно интересоваться музыкой Лазин начинает в 12 лет. Его вдохновителями стали
        британский певец, барабанщик и автор песен Фил Коллинз, американский хип-хоп-исполнитель 
        The Notorious B.I.G. и рэпер Jay Electronica.</p>
    

        <img src="''' + url_for('static', filename='Mnogoznaal.png') + '''">
    </body>
</html>
'''
@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
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

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
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
@app.route('/lab2/example')
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
   
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@app.route('/lab2/add_flower/', defaults={'name': None})
def add_flower_with_default(name):
    if not name:
        return "Вы не задали имя цветка", 400
    return add_flower(name)


@app.route('/lab2/all_flowers')
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

@app.route('/lab2/clear_flowers')
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

@app.route('/lab2/calc/<int:a>/<int:b>')
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

@app.route('/lab2/calc/')
def calc_default_redirect():
    return redirect(url_for('calc', a=1, b=1))

@app.route('/lab2/calc/<int:a>')
def calc_with_redirect(a):
    return redirect(url_for('calc', a=a, b=1))

@app.route('/lab2/books')
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

@app.route('/lab2/cars')
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