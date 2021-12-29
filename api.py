from flask import request, jsonify, Blueprint
from flask_cors import cross_origin
from flask_login import login_required

from model.hero_details import HeroDetails, HeroAppearance, HeroBiography
from service import hero_service

api = Blueprint('api', __name__)


def get_edit_from_request() -> HeroDetails:
    name = request.json['name']
    appearance = HeroAppearance(
        request.json['appearance']['gender'],
        request.json['appearance']['race'],
        request.json['appearance']['eye_colour'],
        request.json['appearance']['hair_colour']
    )

    biography = HeroBiography(
        request.json['biography']['full_name'],
        "",
        request.json['biography']['place_of_birth'],
        request.json['biography']['alignment'],
        request.json['biography']['occupation'],
    )
    return HeroDetails(0, name, appearance, biography)


@cross_origin
@login_required
@api.route('/api/heroes')
def get_heroes():
    heroes = hero_service.get_heroes()
    return jsonify(heroes)


@cross_origin
@login_required
@api.route('/api/heroes/<int:hero_id>')
def get_hero_by_id(hero_id):
    hero = hero_service.get_hero(hero_id)
    if hero is None:
        return jsonify({}), 404
    return jsonify(hero)


@cross_origin
@login_required
@api.route('/api/heroes', methods=['POST'])
def create_hero():
    edit = get_edit_from_request()
    hero = hero_service.create_hero(edit)
    return jsonify(hero)


@cross_origin
@login_required
@api.route('/api/heroes/<int:hero_id>', methods=['PUT'])
def update_hero(hero_id):
    if not hero_service.hero_exists(hero_id):
        return jsonify({}), 404

    edit = get_edit_from_request()
    hero = hero_service.update_hero(hero_id, edit)
    return jsonify(hero)


@cross_origin
@login_required
@api.route('/api/heroes/<int:hero_id>', methods=['DELETE'])
def delete_hero(hero_id):
    is_deleted = hero_service.delete_hero(hero_id)
    return jsonify('Done', is_deleted)
