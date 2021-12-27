from flask import Flask, url_for, request, redirect, abort, jsonify
import json

app = Flask(__name__, static_url_path='', static_folder='pages')


access_key = 10159556057344463

# heroes = [
#     {'id': 1, 'name': 'Batman'},
#     {'id': 2, 'name': 'Superman'},
#     {'id': 3, 'name': 'Wonder Woman'},
# ]

heroes_file = open('heroes.json')
heroes = json.load(heroes_file)
heroes_file.close

next_id = 4

@app.route('/heroes')
def get_heroes():
    return jsonify(heroes)


@app.route('/heroes/<int:hero_id>')
def get_hero_by_id(hero_id):
    found_heroes = list(filter(lambda t: t['id'] == hero_id, heroes))
    if len(found_heroes) == 0:
        return jsonify({}, 404)
    return jsonify(found_heroes[0])


@app.route('/heroes', methods=['POST'])
def create_hero():
    global next_id
    if not request.json:
        abort(400)

    hero = {
        'id': next_id,
        'name': request.json('name')
    }

    heroes.append(hero)

    next_id += 1
    return jsonify(hero)


@app.route('/heroes/<int:hero_id>', methods=['PUT'])
def update_hero(hero_id):
    found_heroes = list(filter(lambda t: t['id'] == hero_id, heroes))
    if len(found_heroes) == 0:
        return jsonify({}, 404)

    hero = found_heroes[0]

    if 'name' in request.json:
        hero['name'] = request.json('name')
    return jsonify(hero)


@app.route('/heroes/<int:hero_id>', methods=['DELETE'])
def delete_hero(hero_id):
    found_heroes = list(filter(lambda t: t['id'] == hero_id, heroes))
    if len(found_heroes) == 0:
        return jsonify({}, 404)
    heroes.remove(found_heroes[0])
    return jsonify('Done', True)


if __name__ == '__main__':
    app.run(debug=True)
