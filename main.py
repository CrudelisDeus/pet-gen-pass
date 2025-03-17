import json
import os
import sqlite3

class Manager:
    def __init__(self):
        # init db
        self.conn = None
        self.cursor = None
        self.init_db()

    # db operation
    def init_db(self):
        """create db"""
        self.conn = sqlite3.connect('sec.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS resources(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            link TEXT,
            username TEXT NOT NULL,
            password TEXT,
            additional_info TEXT
        )
        ''')
        self.conn.commit()
        self.conn.close()

    def add_to_db(
            self, name='', link = '', username='',
            password='', additional_info=''):
        self.conn = sqlite3.connect('sec.db')
        self.cursor = self.conn.cursor()
        manager.cursor.execute('''
        INSERT INTO resources(
        name, link, username, password, additional_info)
        VALUES(?, ?, ?, ?, ?)
        ''', (
            name, link, username,
            password, additional_info
        ))
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    manager = Manager()
    manager.add_to_db(
        'test', '', 'test3',
        'test4', 'test5'
    )


# import logging
#
# logging.basicConfig(level=logging.DEBUG, filename='test.log', filemode='a')
#
#
# logging.debug("A DEBUG Message")
# print(os.getcwd())
#
# FILE_DIR = "test"
# FILENAME = "test.json"
#
# full_path = os.path.join(os.getcwd(), FILENAME)
#
# if os.path.exists(full_path) and os.path.isfile(full_path):
#
#


# class Manager:
#     def __init__(self):
#         with open(f'{settings.FILENAME}', 'w') as f:
#


# test = Manager()
# test.add('adminsss44', '123')
# test.add('adsmsin2', '123')
#
# print(test.data)

# test = {}
#
# def added_user(user, passwd):
#     test.update({user:passwd})
#     print(test)
#
# # def init_
#
# if __name__ == '__main__':
#     added_user('test', 'test2')
#     added_user('test2', 'test3')