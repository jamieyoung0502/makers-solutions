import os
from flask import Flask, request

app = Flask(__name__)

predefined_names = 'Julia,Alice,Karim'

# @app.route('/count_vowels', methods=['POST'])
# def count_vowels():
#     str = request.form['text']
#     count = sum(1 for char in str if char.lower() in "aeiou")
#     return f'There are {count} vowels in "{str}"'

@app.route('/names', methods=['GET'])
def get_add_name():
    new_names = predefined_names + "," + request.args['add']
    names_list = new_names.split(",")
    return ", ".join(sorted(names_list, key=lambda name: name.lower()))

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
