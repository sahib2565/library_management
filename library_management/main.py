import sqlite3
import argparse

conn = sqlite3.connect('library.db')
c = conn.cursor()

parser = argparse.ArgumentParser(description='Commands to show or take books')
msg = 'type: av(available books,v(view all the books)'
msg += 'or uv(view only unavailable books)'
parser.add_argument('showbooks', metavar='', type=str, help=msg)
parser.add_argument('-g', '--getbook', metavar='', type=str, help='Get a book')
args = parser.parse_args()


def show_allBooks():
    books = c.execute("select author,book_name,availabilty from books")
    print("Author ", '\t\t', "Book", '\t\t', "Availabilty")
    print('--------''\t\t', '--------', '\t\t', "--------")
    for book in books:
        book_info = book[0] + "\t\t" + book[1] + '\t\t' + book[2]
        print(book_info)
    c.execute("select count(book_name) from books")
    print("\nTotal books: ", c.fetchall()[0][0])


if args.showbooks == 'v':
    show_allBooks()
if args.showbooks != 'av' and args.showbooks != 'v' and args.showbooks != 'uv':
    print("The input was not valid")
    print("Type --help to know the commands,if not clear check the README")
    exit(-1)


def main():
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
