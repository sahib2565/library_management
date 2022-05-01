import sqlite3

conn = sqlite3.connect("library.db")

c = conn.cursor()


def main():
    '''
    c.execute("""CREATE TABLE books(
                book_id TEXT PRIMARY KEY,
                author TEXT DEFAULT "UNKNOWN",
                release TEXT DEFAULT "UNKNOWN",
                book_name TEXT NOT NULL,
                availabilty TEXT not NULL
            )""")
    c.execute("""CREATE TABLE un_books(
                id_book TEXT,
                relase_date date NOT NULL
            )""")
    '''
    list_books = [('38907', 'JK Rowling', '26/06/1997', 'Harry Potter:1', 'YES'),
                  ('39893', 'JK Rowling', '02/07/1998', 'Harry Potter:2', 'YES'),
                  ('33375', 'JK Rowling', '08/07/1999', 'Harry Potter:3', 'YES'),
                  ('10978', 'J.R.R Tolkien', '21/09/1937', 'The lord of the rings:1', 'YES'),
                  ('10988', 'J.R.R Tolkien', '29/07/1954', 'The lord of the rings:2', 'YES'),
                  ('87190', 'George Orwell', '08/06/1949', '1984', 'YES')
                  ]
    # c.executemany("INSERT into books values(?,?,?,?,?)", list_books)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
