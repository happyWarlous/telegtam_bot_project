# telegtam_bot_project
Notes bot

Бот для заметок, похожий на Trello, но в Телеграмме. Основная идея в том, что чат с ботом является своего рода "корзиной", в которой можно было бы достаточно легко перенаправлять задачи по контекстным "доскам" и "колонкам" внутри них.

Сейчас он умеет:
  - Создавать доски, колонны в которые можно записывать задачи
  - Удалять каждую из данный структур (кроме структур по умолчанию, подробнее смотри далее)
  - Записывать заметки в виде набора сообщений боту

Что планируется в будущем:
  - Сделать более дружелюбный интерефейс без использования "скриптовых" команд
  - Прикрутить БД для хранения всех задач
  - Перетаскивать задачу из одно места в другое
  - Доделать механику структруры по умолчанию, которое предполагает в себе, что многие функции могут быть вызваны с меньшем количеством
аргументов, преполагая выполнение в неё же
  - Добавить таймер с напоминанием о какой-либо задаче

[arg] - обязательный аргумент
(arg) - не обязательный аргумент, при отстутвтии считается значение по умолчанию. Не реализовано

/help :
Общее
  - /info - Краткая информация о боте
  - /help - Укороченная версия данной аннотации

Доски
  - /createdesk [namedesk] - Создать доску. При первом запуске ставит первую доску, как доску по умолчанию
  - /setdefaultdesk [namedesk] - Выбрать доску по умолчанию
  - /deletedesk [namedesk] - Удалить доску
  - /showdesks - Показать все доски

Колонны
  - /createcolumn (namedesk) [column] - Создать доску. При первом запуске ставит первую колоннку, как колонну по умолчанию
  - /setdefaultcolumn (namedesk) [column] - Выбрать колонну по умолчанию
  - /deletecolumn (namedesk) [column] - Удалить доску из доски
  - /showcolumn (namedesk) - Показать все колонны данной доски

Задачи
  - /showtasks <namedesk> [column] - Показать все задачи данной колонны из данной доски
