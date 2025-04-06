import pyqrcode
import png
from pyqrcode import QRCode
link='www.youtube.com'
url=pyqrcode.create(link)
url.png('kode.link_qrcode.png',scale=6)