import os
import flask
import time
import getData

from schedule import every, repeat, run_pending


app = flask.Flask(__name__)


data = []

def pushToGithub():
    os.system("git add .")
    os.system("git commit -m updata")
    os.system("git push -u origin main")


def get():
    global data
    data = getData.GetData().run()
    bg = ""
    with open('templates/rank.html', 'r', encoding='utf-8') as f:
        bg = f.read()
    with open('docs/rank.html', 'w', encoding='utf-8') as f:
        f.write(bg)
    
    with open('docs/rank.html', 'a', encoding='utf-8') as f:
        for row in data:
            f.write("<tr>\n")
            for item in row:
                f.write("<td> ")
                f.write(str(item)+" ")
                f.write("</td>\n")
            f.write("</tr>\n")
    
    ed = ""
    with open('templates/end.html', 'r', encoding='utf-8') as f:
        ed = f.read()
    with open('docs/rank.html', 'a', encoding='utf-8') as f:
        f.write(ed)



@repeat(every(1000).minutes)
def run():
    get()
    pushToGithub()



if __name__ == "__main__":
    run()
    while True:
        run_pending()
        time.sleep(1)
    