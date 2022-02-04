import qrcode
from qrcode import image




data = "Hello, World I am a programmer "
image = qrcode.make(data)
image.save("C:/Users/Lenovo/Desktop/Python(lover)/Advance Python/qrcode.jpg/")