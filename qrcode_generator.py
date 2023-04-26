
import qrcode


# Creating an instance of QRCode class
qr = qrcode.QRCode(
  version=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,
)

# Data to encode
qr.add_data("https://github.com/wyderkaj")

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.jpg")




