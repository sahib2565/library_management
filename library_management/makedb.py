import sqlite3

conn = sqlite3.connect("library.db")

c = conn.cursor()


def main():
    c.execute("""CREATE TABLE books(
                book_id TEXT PRIMARY KEY,
                author_name TEXT DEFAULT "UNKNOWN",
                author_surname TEXT DEFAULT "UNKNOWN",
                release date DEFAULT "UNKNOWN",
                book_name TEXT NOT NULL,
                availabilty TEXT not NULL
            )""")
    c.execute("""CREATE TABLE un_books(
                id_book TEXT,
                relase_date date NOT NULL
            )""")
    list_books = [('38907', 'JK', 'Rowling', '1997-06-26', 'Harry Potter:1', 'YES'),
                  ('39893', 'JK', 'Rowling', '1998-07-02', 'Harry Potter:2', 'YES'),
                  ('33375', 'JK', 'Rowling', '1999-07-08', 'Harry Potter:3', 'YES'),
                  ('10978', 'J.R.R', 'Tolkien', '1937-09-21', 'The lord of the rings:1', 'YES'),
                  ('10988', 'J.R.R', 'Tolkien', '1954-07-29', 'The lord of the rings:2', 'YES'),
                  ('87190', 'George', 'Orwell', '1949-06-08', '1984', 'YES')
                  ]
    c.executemany("INSERT into books values(?,?,?,?,?,?)", list_books)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
