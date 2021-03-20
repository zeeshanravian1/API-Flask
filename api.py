from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/about')
def about():
    return 'this is our compmay about page'

@app.route('/about/<string:name>/<int:years>')
def customerName(name, years):
    return f'Hello {name}, Your experience in NexAI is {years} years'


if __name__ == '__main__':
    app.run(debug=True)