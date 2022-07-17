#WAP that creates a QR Code for a url.
# 1. Import QRcode
# 2. Create a variable to store the QRCode formula
# 3. Use the imported QR code method accompanied by '.make(url of the website)
# 4. Use the .save function with the variable attached to the front to save your QRcode to your cpu memory
# 5. If you dont want to save it to your cpu memory, create a print function to print it in your terminal

import qrcode
img = qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")
# print(img)