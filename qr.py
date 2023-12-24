from PIL import Image
import qrcode

#Data to be encoded in the QR Code 
data="https://chasfatprojects.netlify.app"
#Generate QR Code 
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)
#Create an Image from the QR Code 
img=qr.make_image(fill_color="black",back_color="white")
#Save the image or display it using PIL's show method
img.save("qr.png")
img.show()