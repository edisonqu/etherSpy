from flask import Flask, render_template, url_for, request

from dotenv import load_dotenv
from etherscan import etherscan_txs

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/sendMessage', methods = ["POST"])
def send_request():
    address = request.json["blockchain"]
    print(request.json)
    #disabling it for the demo
    phone_number = request.json["phone_number"]

    return etherscan_txs(address)

@app.route('/spy')
def spy():  # put application's code here
    return render_template('spy.html')


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
if __name__ == '__main__':
    app.run(debug=True)
