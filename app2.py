from flask import Flask
from flask import render_template
from flask import jsonify
from gevent import pywsgi



app = Flask(__name__)

LOCALDATA = True

@app.route('/data')
def helloWorld():
    return render_template("data.html")


if __name__ == '__main__':

    LOCALDATA = True ##从本地加载数据，不访问数据库或调用API

    app.run(debug=True)
    server = pywsgi.WSGIServer(('0.0.0.0', 12345), app)
    server.serve_forever()

