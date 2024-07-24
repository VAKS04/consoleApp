import json
import os

class Book:
    _id_counter = 1

    def __init__(self,title:str,author:str,year:int,status:str) -> None:
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:

    def __init__(self,filename="library.json") -> None:
        self.library = {}
        self.filename = filename
        self.read_books()
        
    # Проверка на наличие id книги в словаре
    def check_id(self,id:int):
        if id not in self.library.keys():
            return False
        return True

    # Считывание всех данные с файла для последующей индексации  

    def read_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                data = {int(k): v for k,v in data.items()}
                self.library = {**self.library,**data}

            if self.library:
                Book._id_counter = max(self.library.keys()) + 1


    # Добавление книги в файл 
    def add_book(self, value: Book):
        if value.id not in self.library:

            self.library[value.id] = {
                'title':value.title,
                'author':value.author,
                'year':value.year,
                'status':value.status
            }
        else:
            print("Товар с данным id уже существует")
        
        self.save_books()
            
    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump(
                self.library, 
                f, ensure_ascii=False, indent=4)


    # Удаление книги из файла 
    def delete_book(self,id:int):
        if self.check_id(id):
            del self.library[id]
            self.save_books()
        else:
            print('Id введен некоректно')
        
    # Нахождение книги в словаре 
    def search_book(self,title="",author="",year=""):
        d = list()
        if title!="" or author!="" or year!="":
            for k, v in self.library.items():
                for kk,vv in v.items():
                    if title == vv or author ==vv or year == str(vv):
                        d.append(v)
                        break
        return d
            
    
    # Изменение статуса книги в словаре 
    def change_books_status(self,id:int,new_value:str):

        if self.check_id(id):
            self.library[id]['status'] = new_value
            self.save_books()

        else:
            print("Id введен некоректно")

    # Вывести список всех книг
    def list_book(self):
        
        # print("id| title | author | year | status")
        # for k,v in self.library.items():
        #     print(f"{k}  | {v["title"]} | {v["author"]} | {v["year"]} | {v["status"]}")

                # Определение ширины колонок
        column_widths = {
            'id': max(len("id"), *(len(str(k)) for k in self.library.keys())),
            'title': max(len("title"), *(len(v['title']) for v in self.library.values())),
            'author': max(len("author"), *(len(v['author']) for v in self.library.values())),
            'year': max(len("year"), *(len(str(v['year'])) for v in self.library.values())),
            'status': max(len("status"), *(len(v['status']) for v in self.library.values()))
        }

        # Форматирование заголовка таблицы
        header = f"{'id':<{column_widths['id']}} | {'title':<{column_widths['title']}} | {'author':<{column_widths['author']}} | {'year':<{column_widths['year']}} | {'status':<{column_widths['status']}}"
        print(header)
        print("-" * len(header))

        # Форматирование строк таблицы
        for id, book in self.library.items():
            row = f"{id:<{column_widths['id']}} | {book['title']:<{column_widths['title']}} | {book['author']:<{column_widths['author']}} | {book['year']:<{column_widths['year']}} | {book['status']:<{column_widths['status']}}"
            print(row)

