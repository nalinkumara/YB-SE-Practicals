from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nextPage')
def next_page():
    return render_template('page1.html')

@app.route('/learn/<name>')
def learn_page(name):
    return f"{name} is Learning Flask"

@app.route('/learnsince/<name>/<float:years>')
def learn_page_since(name,years):
    return f"{name} is Learning Flask since {years}"
    

if __name__ == '__main__':
    app.run(debug=True)
