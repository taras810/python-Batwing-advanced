class BookDB:
    books = [{"id": "1", "title": "The Shining", "Author":
        "Stephen King"},
             {"id": "2", "title": "The Hobbit", "Author":
                 "J. R. R. Tolkien"}]

    def get_all(self):
        return self.books
