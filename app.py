from flask import Flask, render_template, url_for, request

from dotenv import load_dotenv
from etherscan import etherscan_txs

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
