# from flask_socketio import SocketIO, emit
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#  SocketIO.run(app, debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Your profile information
    profile = {
        'name': 'Vector',
        'occupation': 'Devops engineer',
        'bio': 'Checkout my linkedin'
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)

