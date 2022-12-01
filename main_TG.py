class Desk(str):
    def __new__(cls, input_columns: list, name: str = ''):
        self = super().__new__(cls, name)
        self.columns = input_columns
        self.name = name
        self.count_columns = len(self.columns)
        return self

    def __getitem__(self, item):
        if str(item) == item:
            for j, i in enumerate(self.columns):
                if str(i) == item:
                    return self.columns[j]
        else:
            return self.columns[item]

    def add_column(self, new_column):
        self.columns.append(new_column)
        self.count_columns += 1

    def remove_column(self, removed_column_name):
        self.columns.pop(removed_column_name)
        self.count_columns -= 1

    # @staticmethod
    # def move_task_from_desk(desk_from, column_from, desk_to, column_to, moved_task):
    #     desk_from[column_from].remove_task(moved_task)
    #     desk_to[column_to].add_task(moved_task)

    @staticmethod
    def move_column_from_desk(desk_from, desk_to, moved_column):
        desk_from.remove_column(moved_column)
        desk_to.add_column(moved_column, moved_column)


class Column:

    def __init__(self, input_tasks: list, name: str = ''):
        self.name = name
        self.tasks = input_tasks
        self.count_tasks = len(self.tasks)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.tasks)

    def __len__(self):
        return self.count_tasks

    def __getitem__(self, item):
        if str(item) == item:
            for i in self:
                if str(i) == item:
                    return i
        else:
            return self.tasks[item]

    def add_task(self, new_task):
        self.tasks.append(new_task.body)
        self.count_tasks += 1

    def remove_task(self, removed_task):
        self.tasks.pop(removed_task)
        self.count_tasks -= 1

    @staticmethod
    def move_task_from_column(column_from, column_to, moved_task):
        column_from.remove_task(moved_task)
        column_to.add_task(moved_task)


class Task:

    def __init__(self, body: str):
        self.body = body

    def __str__(self):
        return self.body

    def __repr__(self):
        return self.body
