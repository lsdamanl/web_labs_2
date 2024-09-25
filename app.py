from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
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
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Шипилов Дмитрий Андреевич, лабораторная работа 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <hl>web-сервер на flask</h1>

        <footer>
            &copy; Шипилов Дмитрий Андреевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Шипилов Дмитрий Андреевич, лабораторная работа 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <hl>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</h1>

        <footer>
            &copy; Шипилов Дмитрий Андреевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""