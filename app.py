from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        client = request.form['client']
        rating = request.form['rating']
        comments = request.form['comments']
        print(client, rating, comments)
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()