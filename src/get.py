import urllib.request
import json

# URLからデータを取得する。GETメソッド宛。
def get_json(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            headers = response.getheaders()
            status = response.getcode()

    except urllib.error.URLError as e:
        print(e.reason)
    return json.loads(body)
