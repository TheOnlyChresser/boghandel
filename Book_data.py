import csv
import math
import os
from datetime import datetime

def Truncate(number, decimal):
    faktor = 10 ** decimal
    return math.trunc(number * faktor) / faktor

class Book:

    def __init__(self):
        self.titel = ""
        self.forfatter = ""
        self.aarstal = 0
        #[1 stjerne, 2 stjerner, 3 stjerner...]
        self.ratings = [0,0,0,0,0]
        self.id = -1
        self.antal = 0
    def get_rating(self):
        r = 0

        for i in range(0,len(self.ratings)):
            r += (i+1)*self.ratings[i]

        return Truncate(r/sum(self.ratings), 2)

    def give_rating(self, r):
        if 0 <= r <= 5:
            self.ratings[int(r)-1] += 1
        else:
            print("Fejl, rating er ikke gyldig")


class Books_data:

    def __init__(self, samples = False):
        '''
        Variablen samples bestemmer om alle bøger skal indlæses,
        eller kun en lille del.
        '''
        if samples:
            infile = open('data/samples/books.csv', mode='r', encoding="utf8")
        else:
            infile = open('data/books.csv', mode='r', encoding="utf8")
        reader = csv.DictReader(infile)

        self.books = []
        for book in reader:
            b = Book()
            try:
                b.titel = book["title"]
                b.ratings[0] = int(book["ratings_1"])
                b.ratings[1] = int(book["ratings_2"])
                b.ratings[2] = int(book["ratings_3"])
                b.ratings[3] = int(book["ratings_4"])
                b.ratings[4] = int(book["ratings_5"])
                b.aarstal = int(float(book["original_publication_year"]))
                b.forfatter = book["authors"]
                b.id = int(book['book_id'])
                b.antal = int(book["books_count"])
            except:
                print(book)

            self.books.append(b)
        print("Indlæst {} bøger".format(len(self.books)))

    def get_book_list(self, n=0):
        '''
        Returnerer en liste med n bøger.
        '''
        if n > 0:
            n = min(n, len(self.books)-1)
        else:
            n = len(self.books)-1
        return self.books[0:n]

    def slet_bog(self, b):
        '''
        Slet en bog med et bestemt id
        '''
        for book in self.books:
            if book.id == b.id:
                self.books.remove(book)

    def get_book(self, id):
        '''
        find en bog med et bestemt id
        '''
        book = None
        for b in self.books:
            if b.id == id:
                book = b
        return book

    def gem_koeb(self, kurv_items):
        '''
        Gem et køb til regnskabet i data/regnskab.csv
        '''
        # absolut sti, saa filen altid lander i projektets data-mappe
        regnskab_fil = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'regnskab.csv')
        fil_findes = os.path.exists(regnskab_fil)
        outfile = open(regnskab_fil, mode='a', newline='', encoding='utf8')
        writer = csv.writer(outfile)

        if not fil_findes:
            writer.writerow(["dato", "titel", "pris"])

        dato = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for titel, pris in kurv_items:
            writer.writerow([dato, titel, "{:.2f}".format(pris)])
        outfile.close()

    def update_book(self, b):
        '''
        Opdater oplysningerne om en bog
        '''
        for book in self.books:
            if book.id == b.id:
                book.forfatter = b.forfatter
                book.titel = b.titel
                book.aarstal = b.aarstal
                book.antal = b.antal
