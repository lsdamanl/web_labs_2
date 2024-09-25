from flask import Flask
app = Flask(__name__)

@app.route("/")
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

        <hl> web-сервер на flask</h1>

        <footer>
            &copy; Шипилов Дмитрий Андреевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""