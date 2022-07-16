"""SNSServices"""

import pandas
import requests

if __name__ == "__main__":
    url = "https://api.ssactivewear.com/V2/products"
    response = requests.get(url, auth=("account_number", "token")).json()
    pandas.DataFrame(response).to_excel("products.xlsx")
