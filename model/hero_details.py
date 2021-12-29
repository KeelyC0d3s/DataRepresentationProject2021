from dataclasses import dataclass


@dataclass
class HeroAppearance:
    gender: str
    race: str
    eye_colour: str
    hair_colour: str


@dataclass
class HeroBiography:
    full_name: str
    alter_egos: str
    place_of_birth: str
    alignment: str
    occupation: str


@dataclass
class HeroDetails:
    id: int
    name: str
    appearance: HeroAppearance
    biography: HeroBiography
