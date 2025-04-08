
import requests
import pandas as pd
from pandas.api.types import is_numeric_dtype
import io
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def get_data_1(amount=2000):
    url = 'https://data.gov.il/api/3/action/datastore_search'
    resource_id = '6d3b03e1-de9c-42a8-bb08-91ba564c2f34'

    all_records = []
    limit = 1000

    for offset in range(0, amount, limit):
        params = {
            'resource_id': resource_id,
            'limit': min(limit, amount - offset),
            'offset': offset
        }
        res = requests.get(url, params=params)
        data = res.json()
        records = data['result']['records']
        all_records.extend(records)

        if len(records) < limit:
            break  # no more data

    return all_records

# data fetch of rows . 
def get_data(amount=100):
    url = 'https://data.gov.il/api/3/action/datastore_search'
    params = {
        'resource_id': '6d3b03e1-de9c-42a8-bb08-91ba564c2f34',
        'limit': amount
    }
    res = requests.get(url, params=params)
    data = res.json()
   # print(data)
    records =data['result']['records']
    print("===== new data =====")
    if records:
        headers=list(records[0].keys())
        #print(" | ".join(headers))

        for row in records:
            row_value=[str(row.get(h,"")) for h in headers]
         #   print(" | ".join(row_value))


    return records
#graph fetch logic 
def get_graph(graph_type="bar", colx=None, coly=None, amount=100):
    data = pd.DataFrame(get_data(amount))

    # Validate input
    if graph_type == "histogram":
        if not colx:
            raise ValueError("Histogram requires colx")
        cols_needed = [colx]
    else:
        if not colx or not coly:
            raise ValueError("Graph requires both colx and coly")
        cols_needed = [colx, coly]

    print("this is the cols together", cols_needed)
    filtered_data = data[cols_needed].dropna()
    print("filtered data:\n", filtered_data.head())

    fig, ax = plt.subplots(figsize=(8, 6))

    if graph_type=="Bar Chart" or graph_type=="Column Chart":
        if coly in numerical_columns:
            grouped = filtered_data.groupby(colx)[coly].sum().sort_values(ascending=False).head(10)
            ax.bar(grouped.index, grouped.values)
            ax.set_title(f"Top 10 {colx} by {coly}")
            ax.set_xlabel(colx)
            ax.set_ylabel(coly)
            ax.tick_params(axis='x', rotation=45)
            plt.subplots_adjust(left=0.25)
        elif coly not in numerical_columns:
            grouped = filtered_data.groupby(colx)[coly].size().sort_values(ascending=False).head(10)
            ax.bar(grouped.index, grouped.values)
            ax.set_title(f"Top 10 {colx} by {coly}")
            ax.set_xlabel(colx)
            ax.set_ylabel(coly)
            ax.tick_params(axis='x', rotation=45)
            plt.subplots_adjust(left=0.25)


        # ✅ Format Y-axis to 2 decimal places
        if is_numeric_dtype(filtered_data[coly]):
            ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.2f}'))
        if is_numeric_dtype(filtered_data[colx]):
            ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.2f}'))

    elif graph_type == "Pie Chart" and coly in numerical_columns:
     grouped = filtered_data.groupby(colx)[coly].sum().sort_values(ascending=False).head(10)
     grouped = pd.to_numeric(grouped, errors='coerce').dropna()  # ✅ Fix here
     ax.pie(grouped.values, labels=grouped.index, autopct='%1.2f%%', startangle=140)
     plt.subplots_adjust(left=0.25)
     ax.set_title(f"{coly} Distribution by {colx}")

    elif graph_type == "Pie Chart" and coly not in numerical_columns:
        grouped = filtered_data.groupby(colx)[coly].size().sort_values(ascending=False).head(10)
        grouped = pd.to_numeric(grouped, errors='coerce').dropna()  # ✅ Also safe here
        ax.pie(grouped.values, labels=grouped.index, autopct='%1.2f%%', startangle=140)
        plt.subplots_adjust(left=0.25)
        ax.set_title(f"{coly} Distribution by {colx}")
    

    elif graph_type=="Histogram":
        ax.hist(filtered_data[colx], bins=7, edgecolor='black')
        ax.set_title(f"Histogram of {colx}")
        ax.set_xlabel(colx)
        plt.subplots_adjust(left=0.45)
        ax.set_ylabel("Frequency")

        # ✅ Format Y-axis to 2 decimal places
        if is_numeric_dtype(filtered_data[coly]):
            ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.2f}'))
        if is_numeric_dtype(filtered_data[colx]):
            ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.2f}'))

    else:
        raise ValueError("Unsupported graph type")

    img = io.BytesIO()
    try:
        plt.tight_layout()
    except:
        pass
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return img

numerical_columns = {
    "NISCurrencyAmount",
    "Quantity",
    "VAT",
    "PurchaseTax",
    "GeneralCustomsTax",
    "IsPreferenceDocument",
    "IsTradeAgreementWithQuota"
}
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
    "General Tax":"GeneralCustomsTax",
    "Purchase Tax":"PurchaseTax"
}




