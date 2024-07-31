import json
import os
from book import Book

class Library:


    def __init__(self, filename="app/library.json") -> None:

        self.library = {}
        self.filename = filename
        self.read_books()

    # Проверка на наличие id книги в словаре
    def check_id(self, id:int):
        if id not in self.library.keys():
            return False
        return True

    # Считывание всех данные с файла для последующей индексации  
    def read_books(self):

        if os.path.exists(self.filename):

            with open(self.filename, 'r') as f:
                data = json.load(f)
                data = {int(k): v for k,v in data.items()}
                self.library = {**self.library, **data}

            if self.library:
                Book._id_counter = max(self.library.keys()) + 1

    # Добавление книги в файл 
    def add_book(self, title, author, year, status):

        book = Book.set_book(title=title,
                             author=author, 
                             year=year, 
                             status=status)
        
        if book!=False:

            self.library[book.id] = {
                'title':book.title.strip(),
                'author':book.author.strip(),
                'year':int(book.year),
                'status':book.status
            }

            self.save_books()

            return True    
        
        return False

    def save_books(self):

        with open(self.filename, 'w') as f:
            json.dump(
                self.library, 
                f, 
                ensure_ascii=False,
                indent=4
            )

    # Удаление книги из файла 
    def delete_book(self, id:int):

        if self.check_id(id):
            del self.library[id]

            self.save_books()

            return True     
           
        return False
        

    # Нахождение книги в словаре 
    def search_book(self, title="", author="", year="",show = False):

        d = dict()

        if (title.strip()!=""
             or author.strip()!="" 
             or year.strip!=""):
            
            for k, v in self.library.items():

                for kk,vv in v.items():

                    if (title.lower().strip() == str(vv).lower() 
                         or author.lower().strip() == str(vv).lower()
                         or year.strip() == str(vv)):
                        
                        d[k] = v

                        break

        if d:
            if show != False:

                self.table(d=d)

            return True
        
        return False
    
    # Изменение статуса книги в словаре 
    def change_books_status(self, id:int, new_value:str):

        if self.check_id(id):
            new_status = Book.status_book(new_value)

            if (new_status != False):
                self.library[id]['status'] = new_status
                
                self.save_books()

                return True 
                   
        return False


    def table(self,d = None):

        library = (self.library if d == None else d)

        column_widths = {
            'id': (
                max(len("id"), 
                    *(len(str(k)) for k in library.keys()))),
            'title': (
                max(len("title"), 
                    *(len(v['title']) for v in library.values()))),
            'author':( 
                max(len("author"),
                    *(len(v['author']) for v in library.values()))),
            'year': (
                max(len("year"), 
                    *(len(str(v['year'])) for v in library.values()))),
            'status': (
                max(len("status"), 
                    *(len(v['status']) for v in library.values())))
        }

        # Форматирование заголовка таблицы
        header = (f"{'id':<{column_widths['id']}}"
                  + f" | {'title':<{column_widths['title']}}"
                  + f" | {'author':<{column_widths['author']}}"
                  + f" | {'year':<{column_widths['year']}}"
                  + f" | {'status':<{column_widths['status']}}")
        
        print(header)

        print("-" * len(header))
        # Форматирование строк таблицы
        for id, book in library.items():

            row = (f"{id:<{column_widths['id']}}"
                   + f" | {book['title']:<{column_widths['title']}}"
                   + f" | {book['author']:<{column_widths['author']}}"
                   + f" | {book['year']:<{column_widths['year']}}"
                   + f" | {book['status']:<{column_widths['status']}}")
            
            print(row)

    # Вывести список всех книг
    def list_book(self):

        self.table()