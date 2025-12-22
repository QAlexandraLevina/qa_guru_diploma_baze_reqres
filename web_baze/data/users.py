import dataclasses


@dataclasses.dataclass
class UserData:
    mail: str
    password: str
    promo_code: str = None