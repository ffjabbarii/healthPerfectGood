import datetime

from flask import Flask, jsonify
app = Flask(__name__)
start = datetime.datetime.now()


@app.route('/health', methods=['GET'])
def health():
    delta = datetime.datetime.now() - start
    code = 500 if delta.seconds > 60 else 200
    res = {'result': 'OK'} if code == 200 else {'result': 'Failure'}

    print(f'/health {code}')
    return jsonify(res), code


@app.route('/ready', methods=['GET'])
def ready():
    delta = datetime.datetime.now() - start
    code = 200 if delta.seconds > 20 else 500
    res = {'result': 'OK'} if code == 200 else {'result': 'Failure'}

    print(f'/ready {code}')
    return jsonify(res), code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
