userIds = [
    14241500012,
    14241400063,
    14241400001,
    14241500046,
    14241500045,
    14241500028,
    14241500080,
    14241400113,
    14241400073,
    14241500041,
    14241500052,
    14241400152,
    14241500055,
    14241400080,
    14241400156,
    14241500014
]

import requests
import json
import time
import functools
import csv
import datetime

class GetData:
    def __init__(self):
        self.URL = "https://oj.hnist-acm.com/api/profile?username={}"
        self.headers = {
            'cookie': "_ga=GA1.2.1523282867.1726501772; csrftoken=7Tk6cq4x2ahF3rHZ3cMSH4dUslR2nM1hTFVPGHcuc155Qc734J0R28HyHNoJnRzO; sessionid=0lnjfx2bacirn7g1ja3dbkdotl0xxvag; _gid=GA1.2.251085618.1727367701; _ga_59QEB25NR7=GS1.2.1727367701.3.1.1727367724.0.0.0",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
        }
        self.datas = []

        for userId in userIds:
            try:
                Id = str(userId)
                url = self.URL.format(Id)
                r = requests.get(url=url, headers=self.headers)
                js = json.loads(r.text)
                data = [js['data']["real_name"], 
                        js['data']['user']["username"],
                        js['data']["userclass"],
                        js['data']['accepted_number'],
                        js['data']["submission_number"]]
                self.datas.append(data)
                time.sleep(0.5)
            except:
                print(userId)

    def cmp(self, x, y):
        if x[3] == y[3]:
            if x[4] > y[4]:
                return 1
            elif x[4] < y[4]:
                return -1
            else:
                return 0
        elif x[3] < y[3]:
            return 1
        else:
            return -1

    def run(self):
        self.datas.sort(key=functools.cmp_to_key(self.cmp))
        self.write()
        return self.datas
    
    
    def write(self):
        now = str(datetime.datetime.now().strftime('%Y-%m-%d_%H时%M分%S秒'))
        fileName = 'data/' + now + ".csv"
        with open(file=fileName, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.datas)