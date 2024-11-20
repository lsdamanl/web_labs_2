from flask import Blueprint, render_template, request, redirect, session, url_for
lab5 = Blueprint('lab5',__name__)


@lab5.route('/lab5/')
def main():
    username = session.get('username', 'Anonymous')
    return render_template('lab5/lab5.html', username=username)


@lab5.route('/lab5/login')
def login():
    return render_template('lab5/login.html')


@lab5.route('/lab5/register')
def register():
    return render_template('lab5/register.html')


@lab5.route('/lab5/list')
def articles_list():
    return render_template('lab5/list.html')


@lab5.route('/lab5/create')
def create_article():
    return render_template('lab5/create.html')