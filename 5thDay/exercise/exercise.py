class LibraryItem:
    
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def display_info(self):
        pass
    
class Book(LibraryItem):
    
    def __init__(self, title, author, publication_year, genre, isbn):
        self.genre = genre
        self.isbn = isbn
        super().__init__(title, author, publication_year)
    
    def display(self):
        print("Book title: ", self.title, ", Book author: ", self.author, ", Book publication: ", self.publication_year, ", Book genre: ", self.genre, ", Book isbn:", self.isbn)
        
class Magazine(LibraryItem):
    
    def __init__(self, title, author, publication_year, date):
        self.date = date
        super().__init__(title, author, publication_year)
    
    def display(self):
        print("Magazine title: ", self.title, ", Magazine author: ", self.author, ", Magazine publication: ", self.publication_year, ", Magazine date", self.date)
        
        
book_1 = Book("Madolduwa", "Munidasa", "2010", "Adventure", 761236123)
magazine_1 = Magazine("Evo", "Unknown", "2001", "2002/12/1")

book_1.display()
magazine_1.display()    