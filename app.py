from flask import Flask, render_template

socketio = Flask(__name__)

@socketio.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(debug=False)