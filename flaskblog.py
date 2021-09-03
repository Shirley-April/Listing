from flask import Flask, render_template

app = Flask(__name__)   

posts = [
    {
        'author':'Sam',
        'title':'Blog Post 1',
        'content':'blablabla',
        'date_posted': 'Jun 23 2029'
    },
    {
        'author':'Brad',
        'title':'Blog Post 2',
        'content':'blablabla',
        'date_posted': 'Jun 23 2029'
    }
]

@app.route('/')
def index():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)