from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1, 255)
    return render_template('index.html', number=random_num)

if __name__ == '__main__':
    app.run(debug=True)
