from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:  
            error = "Пожалуйста, введите имя"
            return render_template('lab9/index.html', error=error)
        return redirect(url_for('lab9.ask_age', username=username))
    return render_template('lab9/index.html')


@lab9.route('/lab9/age/', methods=['GET', 'POST'])
def ask_age():
    username = request.args.get('username')
    if not username:  
        return redirect(url_for('lab9.main'))  
    if request.method == 'POST':
        age = request.form.get('age')
        if not age or not age.isdigit():  
            error = "Пожалуйста, введите корректный возраст"
            return render_template('lab9/age.html', username=username, error=error)
        return redirect(url_for('lab9.ask_gender', username=username, age=age))
    return render_template('lab9/age.html', username=username)


@lab9.route('/lab9/gender/', methods=['GET', 'POST'])
def ask_gender():
    username = request.args.get('username')
    age = request.args.get('age')
    if not username or not age:  
        return redirect(url_for('lab9.main'))  
    if request.method == 'POST':
        gender = request.form.get('gender')
        if not gender:
            error = "Пожалуйста, выберите ваш пол"
            return render_template('lab9/gender.html', username=username, age=age, error=error)
        return redirect(url_for('lab9.preferences', username=username, age=age, gender=gender))
    return render_template('lab9/gender.html', username=username, age=age)


@lab9.route('/lab9/preferences/', methods=['GET', 'POST'])
def preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    if not username or not age or not gender: 
        return redirect(url_for('lab9.main'))  
    if request.method == 'POST':
        choice = request.form.get('choice')
        return redirect(url_for('lab9.more_preferences', username=username, age=age, gender=gender, choice=choice))
    return render_template('lab9/preferences.html', username=username, age=age, gender=gender)


@lab9.route('/lab9/more_preferences/', methods=['GET', 'POST'])
def more_preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    choice = request.args.get('choice')  

    if not username or not age or not gender or not choice:
        return redirect(url_for('lab9.main'))

    if request.method == 'POST':
        more_choice = request.form.get('more_choice')

        age = int(age)
        if age < 18:
            age_group = 'child'
        else:
            age_group = 'adult'

        if gender == 'male':
            pronoun = "прекрасный мальчик" if age_group == 'child' else "прекрасный мужчина"
        else:
            pronoun = "наимилейшая девочка" if age_group == 'child' else "наимилейшая женщина"

        if choice == "что-то вкусное":
            if more_choice == "сладкое":
                gift_image = "candies.jpg"
                wish = "наслаждаться сладкими моментами жизни, как новогодними конфетами"
            elif more_choice == "сытное":
                gift_image = "japan.jpg"
                wish = "никогда не знать голода и всегда находить что-то вкусное, даже в самый загруженный день"
        elif choice == "что-то красивое":
            if more_choice == "природа":
                gift_image = "nature.jpg"
                wish = "находить вдохновение в красоте природы, как в зимнем лесу под снежным покровом"
            elif more_choice == "искусство":
                gift_image = "art.jpg"
                wish = "видеть красоту во всем, как художник, создающий шедевр"

        congratulation = f"Желаю тебе, {username}, {wish}. Вот тебе подарок!"
        return render_template('lab9/congratulations.html', username=username, age=age,
            pronoun=pronoun, congratulation=congratulation, gift_image=gift_image)

    return render_template('lab9/more_preferences.html', username=username, age=age,
        gender=gender, choice=choice)