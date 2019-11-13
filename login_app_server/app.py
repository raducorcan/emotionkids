import os
import random
import string

from flask import Flask, request, jsonify
from flask_cors import CORS

from login import recognise

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './static/unknown'


def generateFilename():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(100))


@app.route("/", methods=['GET'])
def hello():
    return "HELLO"


@app.route("/login", methods=['POST'])
def fileUpload():
    f = request.files['image']
    filename = generateFilename() + ".png"
    filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(filename)

    name = recognise(filename)
    response = {'name': name}
    return jsonify(response)


if __name__ == '__main__':
    app.run()