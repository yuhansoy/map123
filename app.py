from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    if not name:
        return redirect(url_for('index'))
    return f'Hello, {name}!'

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
