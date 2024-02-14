from typing import List

from models import Note


class TempBase:
    '''Класс базы данных в оперативной памяти.'''

    def __init__(self):
        self.current_id: int = 0

    def count_notes(self) -> int:
        '''Получить количество записей в файле.'''
        return len(file.readlines())

    def get_note(self, id: int) -> Note:
        '''Получить запись по id.'''
        data = file.readlines()[id]
        note = [line.strip() for line in data.split(' / ')]
        object = Note(
            last_name=note[1],
            first_name=note[2],
            patronymic=note[3],
            organization=note[4],
            work_phone=note[5],
            mobile_phone=note[6],
        )
        return object

    def post_note(self, note: Note) -> None:
        '''Добавление записи.'''
        file.write(str(self.current_id) + ' / ' + str(note))
        self.current_id += 1

    def search_note(self, query: List[str]) -> List[str]:
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
