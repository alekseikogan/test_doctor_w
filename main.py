from commands import COMMANDS


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

        key = query[1]
        value = query[2]
        if self.transactions:
            self.transactions[-1][key] = value
        else:
            self.storage[key] = value

    def get_note(self, query) -> None:
        '''Возвращает ранее сохраненную переменную.
           Пример запроса-query: ['GET', 'A']'''

        if self.transactions:
            result = self.transactions[-1].get(query[1], 'NULL')
            print(result)
            return

        result = self.storage.get(query[1], 'NULL')
        print(''.join(result))

    def unset_note(self, query) -> None:
        '''Удаляет ранее установленную переменную.
           Пример запроса-query: ['UNSET', 'A']'''

        if self.transactions:
            del self.transactions[-1][query[1]]
        elif query[1] in self.storage:
            del self.storage[query[1]]

    def counts_note(self, query) -> None:
        '''Подсчитывает количество переменных с заданным значением.
           Пример запроса-query: ['COUNTS', '10']'''

        if self.transactions:
            counter = list(self.transactions[-1].values()).count(query[1])
            print(counter)
            return

        print(list(self.storage.values()).count(query[1]))

    def find_note(self, query) -> None:
        '''Выводит найденные установленные переменные для
           данного значения.
           Пример запроса-query: ['FIND', '10']'''

        if self.transactions:
            result = [key for key, value in self.transactions[-1].items() if value == query[1]]
            print(' '.join(result))
            return

        result = [key for key, value in self.storage.items() if value == query[1]]
        print(' '.join(result))

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

        if self.transactions:
            current_trans = self.transactions.pop()
            for key, value in current_trans.items():
                if value is not None:
                    self.storage[key] = value
                else:
                    del self.storage[key]

    def rollback_note(self, query) -> None:
        '''Отменяет транзакцию.
           Пример запроса-query: ['ROLLBACK']'''

        if self.transactions:
            self.transactions.pop()

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


def main() -> None:
    '''Главная функция - запуск интерфейса в терминале.'''

    terminal = Terminal()
    terminal.run()


if __name__ == '__main__':
    main()
