
from flask import Flask, jsonify, render_template, request ,send_file
from suportB.dataManagment import get_data, get_graph ,get_data_1
import pandas as pd
import matplotlib.pyplot as plt

import io

Server = Flask(__name__,static_folder='supportFE')

@Server.route('/')
def index():
    return render_template('mainHtml.html')

@Server.route('/api/data')
def api_data():
    amount = request.args.get('amount', default=100, type=int)
    if amount>= 1000:
        data=get_data(amount)
        return jsonify(data)
    else:
        data=get_data_1(amount)       
        return jsonify(data)
    


@Server.route('/api/graph',methods=['POST'])
def api_graph():
    data =request.get_json()
    graph_type=data.get("graphType", "")
    item1=data.get("item1")
    item2=data.get("item2")
    amount=data.get("item3")

    item1=column_map.get(item1)
    item2=column_map.get(item2)

    if not item1 or (graph_type != "historgam" and not item2):
      return jsonify({"error":"missing item1"}),400

    print("===== graph type over here ======" +graph_type) 
    img=get_graph(graph_type,item1,item2,amount)
   

# Return image
    return send_file(img, mimetype='image/png')
        


column_map = {
    "Country": "Origin_Country",
    "HS Code": "CustomsItem_8_Digits",
    "Value": "NISCurrencyAmount",
    "Quantity": "Quantity",
    "CustomsHouse": "CustomsHouse",
    "Year": "Year",
    "Month": "Month",
    "Measurement Unit": "Quantity_MeasurementUnitName",
    "Currency": "CurrencyCode",
    "VAT": "VAT",
    "Purchase Tax": "PurchaseTax",
    "General Customs Tax": "GeneralCustomsTax",
    "Agreement": "TradeAgreementName",
    "Terms of Sale": "TermsOfSale",
    "General Tax":"GeneralCustomsTax good",
    "Purchase Tax":"PurchaseTax"
}
numerical_columns = {
    "NISCurrencyAmount",
    "Quantity",
    "VAT",
    "PurchaseTax",
    "GeneralCustomsTax",
    "IsPreferenceDocument",
    "IsTradeAgreementWithQuota"
}
if __name__ == '__main__':
    Server.run(debug=True)