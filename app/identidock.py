from flask import Flask
app = Flask(__name__)

@app.route('/')
def random():
    return 'When asked if Abe had any hobbies, Mary Todd Lincoln said, Cats.\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
