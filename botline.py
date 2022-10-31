import requests
from datetime import datetime as d
import time


def main(message):
    """Main Function"""
    url = 'https://notify-api.line.me/api/notify'
    token = 'BrH2FVCNC48KzV29ieRwLWrHd9mrEnLyqtEDw2jte3y'
    header = {'content-type': 'application/x-www-form-urlencoded',
              'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=header, data=message)


url = 'https://api.bitkub.com'
price = 0
mycoin = ['THB_BTC', 'THB_ETH', 'THB_DOGE']
date = d.now()
day = date.strftime("%Y-%m-%d %H:%M")

while True:
    req = requests.get(url + '/api/market/ticker')
    data = req.json()
    for i in mycoin:
        coin = data[i]
        last = coin['last']
        high = coin['high24hr']
        low = coin['low24hr']
        if price != last:
            msg = f"{day} \n" \
                  f"ตอนนี้ {i} \n" \
                  f"ราคาล่าสุดอยู่ที่ : {last} \n" \
                  f"----------- \n" \
                  f"24 H สูงสุด : {high} \n" \
                  f"24 H ต่ำสุด : {low} \n" \
                  f"----------- \n"
            price = last
            main({'message': msg})
    time.sleep(60)
