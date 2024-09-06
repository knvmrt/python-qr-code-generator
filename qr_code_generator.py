import qrcode
from PIL import Image

# We ask the user to enter a URL
data = input("Please enter a URL: ")

# We create QR code
qrCode = qrcode.QRCode(version=1, box_size=10, border=5)
qrCode.add_data(data)
qrCode.make(fit=True)

# We create the QR code image
image = qrCode.make_image(fill="black", back_color="white")

# We save the QR code
image.save("qr_code.png")

# We open the generated QR code
Image.open("qr_code.png").show()