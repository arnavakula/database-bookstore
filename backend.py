import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        self.conn.commit()
        
    def add(self, title, author, year, isbn):
        self.cursor.execute('INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)' , (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cursor.execute('SELECT * FROM bookstore')
        content = self.cursor.fetchall()
        return content

    def search(self, title = '', author = '', year = '', isbn =''):
        self.cursor.execute('SELECT * FROM bookstore WHERE title = ? OR author = ? OR year = ? OR isbn = ?', (title, author, year, isbn))
        content = self.cursor.fetchall()
        return content

    def delete(self, id):
        self.cursor.execute('DELETE FROM bookstore WHERE id = ?', (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute('UPDATE bookstore SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?', (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()