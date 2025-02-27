from flask import Flask

from user_api import user_router
from book_api import book_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(book_router)

status_code_created = 201


@app.route('/')
def index():
    return "hello world"

@app.errorhandler(404)
def page_not_found(error):
    return "This resource does not exists", 404


if __name__ == '__main__':
    app.run(debug=True)
