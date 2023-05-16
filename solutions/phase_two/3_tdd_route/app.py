import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    str = request.form['text']
    count = sum(1 for char in str if char.lower() in "aeiou")
    return f'There are {count} vowels in "{str}"'












if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
