from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)

@lab1.route("/lab1")
def lab():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
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


@lab1.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
        <title>Дуб</title>
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='/lab1/oak.jpg') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>О студенте</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
    </head>
    <body>
        <h1>Шипилов Дмитрий Андреевич</h1>
        <h2>Группа ФБИ-24, 3 курс</h2>
        <img src="''' + url_for('static', filename='/lab1/nstu.png') + '''">
    </body>
</html>
'''


@lab1.route("/lab1/python")
def python_info():
    return '''
<!doctype html>
<html>
    <head>
        <title>О языке Python</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
    </head>
    <body>
        <h1>Python</h1>
        <p>Python — это высокоуровневый язык программирования, отличающийся эффективностью, простотой и универсальностью использования.
        Он широко применяется в разработке веб-приложений и прикладного программного обеспечения, а также в машинном
        обучении и обработке больших данных. За счет простого и интуитивно понятного синтаксиса является одним из распространенных языков для обучения программированию. </p>

        <p>Python активно используется в таких областях, как веб-разработка, анализ данных, машинное обучение и автоматизация. 
        Благодаря простому синтаксису и большому количеству библиотек, Python стал одним из самых популярных языков программирования.</p>

        <img src="''' + url_for('static', filename='/lab1/python.png') + '''">

    </body>
</html>
'''


@lab1.route("/lab1/Mnogoznaal")
def custom():
    return '''
<!doctype html>
<html>
    <head>
        <title>Mnogoznaal</title>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='/lab1/lab1.css') + '''">
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
    

        <img src="''' + url_for('static', filename='/lab1/Mnogoznaal.png') + '''">
    </body>
</html>
'''