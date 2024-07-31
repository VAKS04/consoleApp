from datetime import datetime

class Book:

    
    _id_counter = 1

    def __init__(
            self, title:str, author:str, 
            year:int, status:str) -> None:
        
        self.id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @staticmethod
    def status_book(status):

        if (int(status)==1):
            return 'в налиии'
        elif (int(status)==2):
            return 'выдана'
        else:
            return False

    @staticmethod
    def set_book(
            title, author,
            year, status):
        
        if (title=="" or author=="" or year=="" or status==""):
            return False
        
        try:
            if int(year) > int(datetime.now().year) or int(year) < 0:
                return False

            status_str = Book.status_book(status)

            if status_str == False:
                return False
            
        except:
            return False
            
        return Book(title=title,
                    author=author,
                    year=int(year),
                    status=status_str)