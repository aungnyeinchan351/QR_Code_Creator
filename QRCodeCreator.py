import pyqrcode 
import png 
from pyqrcode import QRCode 
content = input("Enter something to create QR code : ")
qr = pyqrcode.create(content)
name = input("Name your png file : ")
qr.png(name+".png", scale = 6)
print("QR code Successfully created.")