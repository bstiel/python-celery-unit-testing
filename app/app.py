import os
from flask import Flask, Response, request, jsonify
from tasks import fetch_data


PATH = './data'
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fetch_data.s(url=request.json['url']).delay()
        return jsonify({'url': request.json['url']}), 201

    data = os.listdir(PATH) if os.path.exists(PATH) else []
    return jsonify(data) 


@app.route('/<string:slug>', methods=['GET', 'POST'])
def get(slug):
    with open(os.path.join(PATH, slug)) as f:
        return Response(f.read(), mimetype='text')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)