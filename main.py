from flask import Blueprint, render_template
from flask_login import login_required

from service import hero_service

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@login_required
@main.route('/heroes')
def heroes():
    heroes = hero_service.get_heroes()
    return render_template('heroes.html', heroes=heroes)


@login_required
@main.route('/heroes/create')
def create_hero():
    return render_template('create_hero.html')


@login_required
@main.route('/heroes/<int:hero_id>/edit')
def edit_hero(hero_id):
    hero = hero_service.get_hero(hero_id)
    return render_template('edit_hero.html', hero=hero)
