import sqlite3
import argparse

conn = sqlite3.connect('library.db')
c = conn.cursor()

parser = argparse.ArgumentParser(description='Commands to show or take books')
msg = 'type: av(available books,v(view all the books)'
msg += 'or uv(view only unavailable books)'
parser.add_argument('showbooks', metavar='', type=str, help=msg)
parser.add_argument('-g', '--getbook', metavar='', type=str, help='Get a book')
msg2 = 'Type: adate(sort by relase date[ascending]),author(sort by author)'
msg2 += ',ddate(sort by relase date[descending])'
parser.add_argument('-s', '--sortby', metavar='', type=str, help=msg)
args = parser.parse_args()


def show_allBooks(mode=None):
    msg = "select author_name,author_surname,book_name,availabilty from books"
    if mode is None:
        print("LOl")
        books = c.execute(msg)
        print("Author ", '\t\t', "Book", '\t\t', "Availabilty")
        print('--------''\t\t', '--------', '\t\t', "--------")
        for book in books:
            book_info = book[0] + " " + book[1] + "\t\t" + book[2] + '\t\t'
            book_info += book[3]
            print(book_info)
        c.execute("select count(book_name) from books")
        print("\nTotal books: ", c.fetchall()[0][0])
    elif mode == "adate":
        books = c.execute("""select release,author_name,author_surname,book_name,availabilty from books
                         order by release ASC""")
        print("Relase", '\t'*3, "Author", '\t'*2, "Book", '\t\t', "Availabilty")
        print('--------''\t\t', '--------', '\t\t', "--------", '\t\t', "-"*7)
        for book in books:
            book_info = book[0] + " " + book[1] + "\t\t" + book[2] + '\t\t'
            book_info += book[3]
            print(book_info)
        c.execute("select count(book_name) from books")
        print("\nTotal books: ", c.fetchall()[0][0])
    elif mode == "ddate":
        books = c.execute("""select release,author_name,author_surname,book_name,availabilty from books
                         order by release DESC""")
        print("Relase", '\t'*3, "Author", '\t'*2, "Book", '\t\t', "Availabilty")
        print('--------''\t\t', '--------', '\t\t', "--------", '\t\t', "-"*7)
        for book in books:
            book_info = book[0] + " " + book[1] + "\t\t" + book[2] + '\t\t'
            book_info += book[3]
            print(book_info)
        c.execute("select count(book_name) from books")
        print("\nTotal books: ", c.fetchall()[0][0])
    else:
        books = c.execute(f"""select author_name,author_surname,book_name,availabilty from books
                         where author_name == '{mode}'""")
        print("Author ", '\t\t', "Book", '\t\t', "Availabilty")
        print('--------''\t\t', '--------', '\t\t', "--------")
        for book in books:
            book_info = book[0] + " " + book[1] + "\t\t" + book[2] + '\t\t'
            book_info += book[3]
            print(book_info)
        c.execute(f"""select count(book_name) from books
        where author_name == '{mode}'""")
        print("\nTotal books: ", c.fetchall()[0][0])
    # conn.commit()


def show_available():
    books = c.execute("""select author,book_name from books
    where availabilty == 'YES'""")
    print("Author ", '\t\t', "Book")
    print('--------''\t\t', '--------')
    for book in books:
        book_info = book[0] + '\t\t' + book[1]
        print(book_info)
    c.execute("select count(book_name) from books")
    print("\nTotal available books: ", c.fetchall()[0][0])
    # conn.commit()


def show_un():
    books = c.execute("""select author,book_name,relase_date from books,un_books
                     where id_book == book_id""")
    print("Author ", '\t\t', "Book", '\t\t', "You can get it after")
    print('--------''\t\t', '--------', '\t\t', "--------")
    for book in books:
        book_info = book[0] + '\t\t' + book[1] + '\t\t' + book[2]
        print(book_info)
    c.execute("select count(*) from un_books")
    print("\nTotal unavailable books: ", c.fetchall()[0][0])


if args.showbooks == 'uv':
    show_un()
if args.showbooks == 'av':
    show_available()
if args.showbooks == 'v':
    show_allBooks(args.sortby)
if args.showbooks != 'av' and args.showbooks != 'v' and args.showbooks != 'uv':
    print("The input was not valid")
    print("Type --help to know the commands,if not clear check the README")
    exit(-1)


def main():
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
