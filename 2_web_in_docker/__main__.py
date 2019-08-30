from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', message=os.getenv('message'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
