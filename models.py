
class Note():
    '''Объект записи в базе данных.'''

    def __init__(self, name, value) -> None:

        self.name: str = name
        self.value: str = value

    def __str__(self) -> str:
        '''Строковое представление записи.'''

        return self.value
