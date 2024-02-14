from utils import COMMANDS


class Terminal():
    '''Терминал с интерфейсом.'''

    def __init__(self) -> None:

        self.commands: dict = COMMANDS
        self.storage: dict = {}  # База данных
        self.transactions: list = []  # Текущая транзакция

    def all_commands(self) -> None:
        '''Вывод списка доступных команд.'''
        for name, helptext in self.commands.items():
            print(f'{name} - {helptext[-1]}')
        print()

    def set_note(self, query) -> None:
        '''Добавляет запись в БД.
           Пример запроса-query: ['SET', 'A', '10']'''

        param = query[1]
        value = query[2]
        if self.transactions:
            self.transactions[-1][param] = value
        self.storage.append((param, value))

    def get_note(self, query) -> None:
        '''Возвращает ранее сохраненную переменную.
           Пример запроса-query: ['GET', 'A']'''
        return self.storage.get(query[1], 'NULL')

    def unset_note(self, query) -> None:
        '''Удаляет ранее установленную переменную.
           Пример запроса-query: ['UNSET', 'A']'''

        pass

    def counts_note(self, query) -> None:
        '''Подсчитывает количество переменных с заданным значением.
           Пример запроса-query: ['COUNTS', '10']'''
        pass

    def find_note(self, query) -> None:
        '''Выводит найденные установленные переменные для
           данного значения.
           Пример запроса-query: ['FIND', '10']'''
        pass

    def end_note(self, query) -> None:
        '''Завершить работу терминала.
           Пример запроса-query: ['END']'''

        print('\nТерминал завершает работу.')
        exit()

    def begin_note(self, query) -> None:
        '''Начинает новую транзакцию.
           Пример запроса-query: ['BEGIN']'''

        self.transactions.append({})

    def commit_note(self, query) -> None:
        '''Подтверждает транзакцию.
           Пример запроса-query: ['COMMIT']'''

        pass

    def rollback_note(self, query) -> None:
        '''Отменяет транзакцию.
           Пример запроса-query: ['ROLLBACK']'''

        pass

    def transaction_depth(self):
        return len(self.transactions)

    def command_detect(self, query: str) -> None:
        '''Обработка и вызов команды.'''

        command = getattr(self, self.commands[query[0]][0])
        command(query)

    def run(self) -> None:
        '''Запустить терминал.'''

        print('Терминал запущен\n')
        print('Доступные команды:\n')
        self.all_commands()

        while True:
            command = input('>' * (self.transaction_depth() + 1)).split()
            if command[0] not in self.commands.keys():
                print('\nТакой команды не существует')
                continue
            self.command_detect(command)
