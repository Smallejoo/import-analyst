
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io

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

def get_graph(graph_type="bar" ,colx=1 ,coly=1,amount=100):
      data=get_data(amount)
      data=pd.DataFrame(data)
      cols_needed=[colx]
      cols_needed.append(coly)
      print("this is the cols togther "+str(cols_needed))
      filterd_data=data[cols_needed].dropna()
      print("filtered data"+str(filterd_data))

      fig,ax=plt.subplots()

      if "bar" in graph_type or "column" in graph_type:
        grouped=filterd_data.groupby(colx)[coly].sum().sort_values(ascending=False).head(10)
        ax.bar(grouped.index, grouped.values)
        ax.set_xlabel(colx)
        ax.set_ylabel(coly)

      img = io.BytesIO()
      plt.tight_layout()
      fig.savefig(img, format='png')
      img.seek(0)
      plt.close(fig)  # clean up memory
      
      return (img)
    





