import os
from datetime import datetime
from books import Book, Library

class ConsoleApp:
    MESSAGE = "Нажмите на любую клавишу для продолжения..."
    START_APP_MENU = [
        "1. Добавление книги",
        "2. Удаление книги",
        "3. Поиск книги",
        "4. Отображение всех книг",
        "5. Изменение статуса книги",
        "0. Выйти из приложения"
    ]

    def __init__(self) -> None:
        self._library = Library()
        self._switch = {
            1:self.add_book_page,
            2:self.del_book_page,
            3:self.search_book_page,
            4:self.list_book_page,
            5:self.change_status_page,
            0:os.system
        }


    # Возврат к главному меню
    def back_to_menu(self)->None:
        input(self.MESSAGE)
        os.system('clear')
        self.start_app()
        

    # Валидатор
    def validator(
            self, min_key,
            max_key, inputMESSAGE="Введите номер : ")->None:
        while True:
            value = int(input(inputMESSAGE))
            if min_key <= value <= max_key:
                return value
            print("Некоретктный ввод. Повторите снова ...")


    # Функция главного меню
    def start_app(self)->None:
        os.system('clear')
        for i in self.START_APP_MENU:
            print(i)
        num = self.validator(0,5)
        if num == 0:
            os.system('exit')
        else:
            self.choose_link(num)
        
    
    def choose_link(self, num)->None:
        os.system('clear')
        self._switch[num]()
    

    # Страница добавление книги 
    def add_book_page(self)->None:
        title = input("Введите название книги : ")
        author = input("Введите имя автора : ")
        while True:
            try:
                year = self.validator(
                    1,int(datetime.now().year),
                    "Введите год выпуска : "
                )
                break
            except ValueError:
                print("Введен некоректный год - Попробуйте снова")

        status_int = self.validator(
            1,2,'Введите статус книги : (1 - "в наличии", 2 - "выдана")'
        )
        status = ('в наличии' if status_int == 1 else 'выдана')
        b = Book(
            title, author,
            year, status
        )
        self._library.add_book(b)
        self.back_to_menu()


    # Удаление книги со страницы
    def del_book_page(self)->None:
        self._library.list_book()
        num = int(input("Введите id удаляемой книги : "))
        self._library.delete_book(num)
        self.back_to_menu()


    # Вывести список всех книг на странице
    def list_book_page(self)->None:
        self._library.list_book()
        self.back_to_menu()


    # Страница поиска книги
    def search_book_page(self)->None:
        print("Если вы ищете книги по одному ключу" 
            + "оставляйте не нужные поля пустыми")
        title = input("Введите название книги : ")
        author = input("Введите автора книги : ")
        year = input("Введите год издания: ")
        self._library.search_book(
            title=title,
            author=author,
            year=year
        )
        self.back_to_menu()


    # Страница изменения статуса книги
    def change_status_page(self)->None:
        self._library.list_book()
        while True:
            num = int(input("Введите id изменяемой книги : "))
            if self._library.check_id(num):
                break
            else:
                print('Id введен некоректно')
        new_status = self.validator(
            1,2,"Введите новый статус (1 - 'в наличии', 2 - 'выдана') : "
        )
        status = ('в наличии' if new_status == 1 else 'выдана')
        self._library.change_books_status(num, status)
        self.back_to_menu()