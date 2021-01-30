import pandas as pd
import numpy as np
import urllib
import requests

url = 'https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&limit=100000'


def read_url(url):
    result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data
# stored in json.
    print(result.keys())
    print(result['success'])
    df1 = pd.DataFrame(result['result']['records'])
    print(df1[(df1.year=='2019')&(df1.level_2=='90 Years & Over')&(df1.level_1=='Total Residents')])
    #print(result['result']['records'])
    #print(result['2019'])
### Todo
# Print out the part where data is stored.


def print_hi(name):
    print(f'Hi {name}')

if __name__ == "__main__":
    read_url(url)