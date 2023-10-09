class User:
    def __init__(self, name, birth_dame, rights) -> None:
        self.__name = name
        self.__birth_dame = birth_dame
        self.__rights = rights

    @property
    def name(self):
        return self.__name

    @property
    def birth_date(self):
        return self.__birth_dame

    @property
    def rights(self):
        return self.__rights

    @rights.setter
    def rights(self, _rights):
        self.__rights = _rights


if __name__ == "__main__":
    user = User("Vasya","10.10.10",7)
    user.rights = 1
    print(user.name, user.rights)