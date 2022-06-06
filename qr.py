import pyqrcode
from pyqrcode import QRCode

page = "https://www.google.com/robots.txt"

url = pyqrcode.create(page)
url.svg("qr.svg", scale=8)
