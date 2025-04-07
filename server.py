
from flask import Flask, jsonify, render_template, request
from suportB.dataManagment import get_data

Server = Flask(__name__,static_folder='supportFE')

@Server.route('/')
def index():
    return render_template('mainHtml.html')

@Server.route('/api/data')
def api_data():
    print("how req looks like  " +str(request.args))
    amount = request.args.get('amount', default=100, type=int)
    print("amount of requested data :" +str(amount))
    data=get_data(amount)
    return jsonify(data)

if __name__ == '__main__':
    Server.run(debug=True)