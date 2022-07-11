from main import db
from models.user import User
from models.movies import Movies

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(User(email="andrii@gmail.com"))
    db.session.commit()
    db.session.add(Movies(title="The Dark Knight"))
    db.session.commit()
    print("created tables")
