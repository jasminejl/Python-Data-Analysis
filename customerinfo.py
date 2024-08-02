
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def sql_table():
    return render_template('main.py')

if __name__ == '__main__':
    app.run(debug=True)

