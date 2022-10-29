import requests


def main(message):
    """Main Function"""
    url = 'https://notify-api.line.me/api/notify'
    token = 'BrH2FVCNC48KzV29ieRwLWrHd9mrEnLyqtEDw2jte3y'
    header = {'content-type': 'application/x-www-form-urlencoded',
              'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=header, data=message)


# ส่งข้อความ
msg = {'message': "Hello World"}

# ส่งสติ๊กเกอร์
sticker = {'message': " ", 'stickerPackageId': 789, 'stickerId': 10855}

# ส่งรูป
url = 'https://s.isanook.com/wo/0/ud/4/20927/d21.jpg'  # ลิ้งรูป
imge = {'message': " ", 'imageThumbnail': url, 'imageFullsize': url}
main(imge)
