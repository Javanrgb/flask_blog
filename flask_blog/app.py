from flask import Flask, escape, request, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Javan Ayoma',
        'title': 'Blog Post 1',
        'content': 'First Blog Posted',
        'date_posted': 'May 5,2022',
    },
    {
        'author': 'Jeremy Okeyo',
        'title': 'Blog Post 2',
        'content': 'Second Blog Posted',
        'date_posted': 'May 6,2022',
    }
]


@app.route('/')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
