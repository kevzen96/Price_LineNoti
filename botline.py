import requests


def main(message):
    """Main Function"""
    url = 'https://notify-api.line.me/api/notify'
    token = 'BrH2FVCNC48KzV29ieRwLWrHd9mrEnLyqtEDw2jte3y'
    header = {'content-type': 'application/x-www-form-urlencoded',
              'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=header, data=message)


url = 'https://api.bitkub.com'
price = 0

while True:
    req = requests.get(url + '/api/market/ticker')
    data = req.json()
    last = data['THB_BTC']['last']
    high = data['THB_BTC']['high24hr']
    low = data['THB_BTC']['low24hr']

    if price != last:
        msg = f"ตอนนี้ Bitcoin \n" \
              f"ราคาล่าสุดอยู่ที่ : {last} \n" \
              f"----------- \n" \
              f"24 H สูงสุด : {high} \n" \
              f"24 H ต่ำสุด : {low} \n" \
              f"----------- \n"
        main({'message': msg})
        price = last

