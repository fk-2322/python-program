import pyqrcode
#import png
from pyqrcode import QRCode
#import qr code from pyqrcode
#string which represents the qr code
s= "https://www.cia.gov/"
#generate qr code
url = pyqrcode.create(s)
#create and save the svg file naming "myqr.svg"
url.svg('myqr.svg',scale=8)
#create and save the png file naming "myqr.png"
#url.png('myqr.png',scale=6)
print("image saved")