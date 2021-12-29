import mysql.connector
from dao import dbconfig as cfg

from model.hero_details import HeroDetails, HeroBiography, HeroAppearance


class HeroDao:
    _db = ""

    def __init__(self):
        self._connect_to_db()

    def _connect_to_db(self):
        self._db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def _get_cursor(self):
        if not self._db.is_connected():
            self._connect_to_db()
        return self._db.cursor()

    def _map_row_to_hero(self, row):
        appearance = HeroAppearance(row[2], row[3], row[4], row[5])
        biography = HeroBiography(row[6], row[7], row[8], row[9], row[10])
        hero = HeroDetails(row[0], row[1], appearance, biography)
        return hero

    def get_heroes(self):
        cursor = self._get_cursor()
        sql = "Select * from heroes order by name"
        cursor.execute(sql)

        heroes = []

        rows = cursor.fetchall()
        cursor.close()

        if rows:
            for row in rows:
                hero = self._map_row_to_hero(row)
                heroes.append(hero)
        return heroes

    def get_hero(self, hero_id):
        cursor = self._get_cursor()
        sql = "Select * from heroes where id = %s"
        values = (hero_id,)
        cursor.execute(sql, values)

        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return None
        else:
            return self._map_row_to_hero(result)

    def create_hero(self, hero_details):
        cursor = self._get_cursor()
        sql = "Insert into heroes(" \
              "name, " \
              "gender, race, eye_colour, hair_colour, " \
              "full_name, place_of_birth, alignment, occupation" \
              ") values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        values = (
            hero_details.name,
            hero_details.appearance.gender,
            hero_details.appearance.race,
            hero_details.appearance.eye_colour,
            hero_details.appearance.hair_colour,
            hero_details.biography.full_name,
            hero_details.biography.place_of_birth,
            hero_details.biography.alignment,
            hero_details.biography.occupation,
        )

        cursor.execute(sql, values)
        self._db.commit()

        hero_id = cursor.lastrowid
        cursor.close()

        return self.get_hero(hero_id)

    def update_hero(self, hero_id: int, hero_details: HeroDetails):
        cursor = self._get_cursor()
        sql = "Update heroes set " \
              "name=%s," \
              "gender=%s, race=%s, eye_colour=%s, hair_colour=%s, " \
              "full_name=%s, place_of_birth=%s, alignment=%s, occupation=%s " \
              "Where id=%s"

        values = (
            hero_details.name,
            hero_details.appearance.gender,
            hero_details.appearance.race,
            hero_details.appearance.eye_colour,
            hero_details.appearance.hair_colour,
            hero_details.biography.full_name,
            hero_details.biography.place_of_birth,
            hero_details.biography.alignment,
            hero_details.biography.occupation,
            hero_id
        )

        cursor.execute(sql, values)
        self._db.commit()

        cursor.close()

        return hero_dao.get_hero(hero_id)

    def delete_hero(self, hero_id):
        cursor = self._get_cursor()
        sql = "Delete from heroes where id = %s"
        values = (hero_id,)
        cursor.execute(sql, values)

        self._db.commit()

        cursor.close()


hero_dao = HeroDao()
