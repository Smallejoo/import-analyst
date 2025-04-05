
import requests

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
        print(" | ".join(headers))

        for row in records:
            row_value=[str(row.get(h,"")) for h in headers]
            print(" | ".join(row_value))


    return records


