from models import Note
from utils import COMMANDS
from typing import List


class Terminal():
    '''Терминал с интерфейсом.'''

    def __init__(self) -> None:

        self.commands: dict = COMMANDS
        self.storage: list = []

    def all_commands(self) -> None:
        '''Вывод списка доступных команд.'''
        for name, helptext in self.commands.items():
            print(f'{name} - {helptext[-1]}')
        print()

    def set_note(self, query) -> None:
        '''СДЕЛАЛ Добавляет аргумент в БД.'''

        param = query[1]
        value = query[2]
        self.storage.append((param, value))

    def get_note(self, query) -> None:

    def search_note(self, query) -> None:
        '''Поиск записьа.'''

        print('Вводите через знак ' + '/' + ' без пробелов', end='')
        print(', если параметров несколько.')

        fields = input('\nВведите данные одной строкой: ').split('/')
        try:
            search_result = self.tempbase.search_note(fields)
        except ValueError as e:
            print(e)
            return
        if len(search_result) == 0:
            print('Результат завершен. Ничего не найдено.\n')
            return
        print(f'Найдено {len(search_result)} совпадений:', end='\n')

        for note in search_result:
            print(note)

    def command_detect(self, query: str) -> None:
        '''Обработка и вызов команды.'''

        command = getattr(self, self.commands[query[0]][0])
        command(query)

    def end_note(self, query) -> None:
        '''Завершить работу терминала.'''

        print('\nТерминал завершает работу.')
        exit()

    def run(self) -> None:
        '''Запустить терминал.'''

        print('Терминал запущен\n')
        print('Доступные команды:\n')
        self.all_commands()

        while True:
            command = input('> ').split()
            print(f'Вы ввели: {command}')
            if command[0] not in self.commands.keys():
                print('\nТакой команды не существует')
                continue
            self.command_detect(command)
    # --------------

    def counts_note(self) -> int:
        '''Получить количество записей в файле.'''
        return len(file.readlines())

    def post_note(self, note: Note) -> None:
        '''Добавление записи.'''
        file.write(str(self.current_id) + ' / ' + str(note))
        self.current_id += 1

    def find_note(self, query: List[str]) -> List[str]:
        '''Поиск записи.'''
        if all(i == '' for i in query):
            raise ValueError('Вы ввели пустой запрос')
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()
            result = []
            for line in data:
                note = line.strip()
                if all(
                    query[i] in note.split(' / ') for i in range(len(query))
                ):
                    result.append(note)
            return result

