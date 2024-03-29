from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Maggie Zheng! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css.html')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    print('Subject entered: ' + request.args.get('subject'))
    print('Course number entered: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()


