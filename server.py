import json
import sys, getopt, os
import pandas as pd
from flask import Flask
from pandas.io.json import json_normalize

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../rpe'))
if not path in sys.path:
    sys.path.insert(1, path)

app = Flask(__name__)


def read_json():
    dataframe = pd.read_json('resources/sample.json', lines=True)
    print(dataframe.head(1).datePublishedObject)


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
    #main(sys.argv[1:])
    read_json()
