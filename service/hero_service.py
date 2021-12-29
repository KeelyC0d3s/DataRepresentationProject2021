from dao.hero_dao import hero_dao
from model.hero_details import HeroDetails


def get_heroes():
    return hero_dao.get_heroes()


def get_hero(hero_id: int):
    return hero_dao.get_hero(hero_id)


def hero_exists(hero_id: int) -> bool:
    return get_hero(hero_id) is not None


def create_hero(hero_details: HeroDetails) -> HeroDetails:
    return hero_dao.create_hero(hero_details)


def update_hero(hero_id: int, hero_details: HeroDetails):
    return hero_dao.update_hero(hero_id, hero_details)


def delete_hero(hero_id: int):
    if not hero_exists(hero_id):
        return False

    hero_dao.delete_hero(hero_id)
    return True
