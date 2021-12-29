from dataclasses import dataclass


@dataclass
class UserDetails:
    id: int
    name: str
    email_address: str
    username: str
    password: str
