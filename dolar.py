from bottle import Bottle , request
import requests
from bs4 import BeautifulSoup


page_template = """
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8"/>
      <title>Dolar sayfasi</title>
    </head>
    <body>
      %(body_text)s
    </body>
  </html>
"""

def home_page():
    url = "http://bigpara.hurriyet.com.tr/doviz/dolar/"
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    n = soup.find("span", {"class":"value up"}).text
    number = n.replace(",",".")
    log = []
    number1 = float(number)
    log.append(0)
    if max(log)<number1:
        q = number1
    log.append(number1)
    content = """
        <h1 style="text-align:center;">DOLAR KURU KAC MI?</h1>
        <center>
            <img src="https://im.haberturk.com/2020/03/13/ver1584103602/2612494_810x458.jpg" alt="dolar with covid" style="width:248px;height:164px;margin-left:auto;margin-right:auto;">
        </center>
        <p style="text-align:center;">SON REKOR</p>
        <p style="text-align:center;">%(ss)f</p>
        <br><br>
        <p style="text-align:center;">SUAN</p>
        <p style="text-align:center;">%(number1)f</p>
    """ % {
        "number1": number1,
        "ss": q
    }
    return  page_template % {"body_text": content}

def create_App():
    app = Bottle()
    app.route("/","GET", home_page)
    return app

application = create_App()
application.run(debug=True)


