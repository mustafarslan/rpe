import sys, getopt, os
from flask import Flask
from flask_cors import CORS
from blueprints.database_blueprint import database_blueprint
from blueprints.client_blueprint import client_blueprint

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../rpe'))
if not path in sys.path:
    sys.path.insert(1, path)

app = Flask(__name__)
CORS(app)
app.register_blueprint(database_blueprint)
app.register_blueprint(client_blueprint)


def main(argv):
    hostname = "localhost"
    port = 1080

    try:
        opts, args = getopt.getopt(argv, "h:p:", ["hostname=", "port="])
    except getopt.GetoptError:
        print("Server.py -h <hostname> -p <port>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--hostname"):
            hostname = arg
        elif opt in ("-p", "--port"):
            port = arg
        else:
            print("server.py -h <hostname> -p <port")

    iport = int(port)
    app.run(host=hostname, port=iport, threaded=True)


if __name__ == '__main__':
    main(sys.argv[1:])

