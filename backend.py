import sqlite3

def connect():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()

def add(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bookstore VALUES (NULL, ?, ?, ?, ?)' , (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bookstore')
    content = cursor.fetchall()
    conn.close()
    return content

def search(title = '', author = '', year = '', isbn =''):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bookstore WHERE title = ? OR author = ? OR year = ? OR isbn = ?', (title, author, year, isbn))
    content = cursor.fetchall()
    conn.close()
    return content

def delete(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM bookstore WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE bookstore SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?', (title, author, year, isbn, id))
    conn.commit()
    conn.close()

    
