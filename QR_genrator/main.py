import qrcode as qr
from PIL import Image



# img = qr.make("https://github.com/Chakrastra")
# img.save("GithubQR.png")

myqr=qr.QRCode(version=1,
               error_correction=2,
               box_size=10,border=4)

myqr.add_data("https://github.com/Chakrastra")
myqr.make(fit=True)

img=myqr.make_image(fill_color="red",back_color="blue")
img.save("updatedGithubQR.png")
