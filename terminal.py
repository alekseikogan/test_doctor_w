from utils import COMMANDS

from .models import Note
from .tempbase import TempBase


class Terminal():
    '''Терминал с интерфейсом.'''

    def __init__(self) -> None:

        self.commands = COMMANDS
        self.tempbase: TempBase = TempBase()

    def all_commands(self) -> None:
        '''Вывод списка доступных команд.'''
        for name, helptext in self.commands.items():
            print(f'{name} - {helptext}')
        print()

    def create_note(self):
        '''Добавить запись.'''

        content = []
        input_text = input('Введите команду: ')
        content.append(input_text)
        try:
            note = Note(*content)
        except ValueError as e:
            print(e)
            return
        self.tempbase.post_note(note)

    def search_note(self) -> None:
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

    def command_detect(self, command: str) -> None:
        '''Обработка и вызов команды.'''

        command = getattr(self, self.commands[command[0]])
        command()

    def stop(self) -> None:
        '''Завершить работу терминала.'''

        print('\nТерминал завершает работу.')
        exit()

    def run(self) -> None:
        '''Запустить терминал.'''

        print('Терминал запущен\n')

        print('\nДоступные команды:\n')
        self.all_commands()
        while True:
            command = [input().split()]
            if command[0] not in self.commands.keys():
                print('\nТакой команды не существует')
                continue
            # передаю целиком и буду парсить
            self.command_detect(command)
