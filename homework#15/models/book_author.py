from database import db


class BookAuthor(db.Model):
    __tablename__ = 'book_author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    books = db.relationship("Book")
    authors = db.relationship("Author")
