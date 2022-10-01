

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self._password: int = hash(password)

    @property
    def password(self) -> int:
        return self._password

    @password.setter
    def password(self, value) -> None:
        self._password = hash(value)

    def check_password(self, password: str) -> bool:
        return hash(password) == self.password



user = User('genndalf', 'qwerty')
print(user.__dict__)

print(user.check_password('QWerTy'))
print(user.check_password('QWERTY'))
print(user.check_password('qwerty'))
