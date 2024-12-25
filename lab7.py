from flask import Blueprint, render_template, request, jsonify

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films = [
    {
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Когда засуха, пыльные бури и вымирание растений приводят\
            человечество к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину \
            (которая предположительно соединяет области пространства-времени через большое расстояние) \
            в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и \
            найти планету с подходящими для человечества условиями."
    },
    {
        "title": "Snatch",
        "title_ru": "Большой куш",
        "year": 2000,
        "description": "Фрэнки Четыре Пальца должен был переправить краденый алмаз из Англии в США\
            своему боссу Эви, но, сделав ставку на подпольный боксерский поединок, \
            он попал в круговорот весьма нежелательных событий. Вокруг него и его груза \
            разворачивается сложная интрига с участием множества колоритных персонажей лондонского \
            дна — русского гангстера, троих незадачливых грабителей, хитрого боксера и угрюмого громилы грозного мафиози.\
            Каждый норовит в одиночку сорвать большой куш."
    },
    {
        "title": "Hachi: A Dog's Tale",
        "title_ru": "Хатико: Самый верный друг",
        "year": 2009,
        "description": "Однажды, возвращаясь с работы, профессор колледжа нашел \
            на вокзале симпатичного щенка породы акита-ину. Профессор и Хатико \
            стали верными друзьями. Каждый день пес провожал и встречал хозяина на вокзале."
    },
    {
        "title": "The Green Mile",
        "title_ru": "Зелёная миля",
        "year": 1999,
        "description": "Пол Эджкомб — начальник блока смертников в тюрьме «Холодная гора»,\
          каждый из узников которого однажды проходит «зеленую милю» по пути к месту казни. \
          Пол повидал много заключённых и надзирателей за время работы. Однако гигант Джон Коффи, \
          обвинённый в страшном преступлении, стал одним из самых необычных обитателей блока."
    },
    {
        "title": "Catch Me If You Can",
        "title_ru": "Поймай меня, если сможешь",
        "year": 2002,
        "description": "Фрэнк Эбегнейл успел поработать врачом, адвокатом и пилотом на \
            пассажирской авиалинии – и все это до достижения полного совершеннолетия в 21 год. \
            Мастер в обмане и жульничестве, он также обладал искусством подделки документов, \
            что в конечном счете принесло ему миллионы долларов, которые он получил по фальшивым чекам. \
            Агент ФБР Карл Хэнрэтти отдал бы все, чтобы схватить Фрэнка и привлечь к ответственности за свои деяния, \
            но Фрэнк всегда опережает его на шаг, заставляя продолжать погоню."
    },
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id], 200
    return {"error": "Film not found"}, 404


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        deleted_film = films.pop(id)
        return {"message": "Film deleted successfully", "film": deleted_film}, 200
    return {"error": "Film not found"}, 404


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()
    if film['description'] == '':
        return {'description': 'Заполните описание'}, 400
    films[id] = film
    return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film or not isinstance(film, dict):
        return {"error": "Неверные данные фильма"}, 400  

    if not film.get('description', '').strip():
        return {"description": "Заполните описание"}, 400  

    if not film.get('title', '').strip() and film.get('title_ru', '').strip():
        film['title'] = film['title_ru']

    films.append(film)
    new_index = len(films) - 1
    return {"message": "Фильм успешно добавлен", "index": new_index}, 201
