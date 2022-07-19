from flask import Flask

from config import Config
from database import db
from book_api import book_router
from author_api import author_router
from book_author_api import book_author


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(book_router)
    app.register_blueprint(author_router)
    app.register_blueprint(book_author)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
