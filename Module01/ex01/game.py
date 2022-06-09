class GotHouse:
    family_name: str
    house_words: str

    def __init__(self, family_name, house_words):
        self.family_name = family_name
        self.house_words = house_words

    def __str__(self):
        return f"{self.family_name} {self.house_words}"


class GotCharacter:
    first_name: str
    is_alive: bool = True
    house: GotHouse = None

    def __init__(self, first_name: str, is_alive: bool):
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        return f"{self.first_name}"


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house.house_words)

    def die(self):
        self.is_alive = False


class Targaryen(GotCharacter):
    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and blood"

    def print_house_words(self):
        print(self.house.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear me Roar"

    def print_house_words(self):
        print(self.house.house_words)

    def die(self):
        self.is_alive = False


class Tyrell(GotCharacter):
    def __init__(self, first_name=None, is_alive=True) -> None:
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Tyrell"
        self.house_words = "Growing Strong"

    def print_house_words(self):
        print(self.house.house_words)

    def die(self):
        self.is_alive = False
