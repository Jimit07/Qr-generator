# create a qr code image for your link

import qrcode as qr
# Here i have used an youtube link .You can use any other link
img = qr.make('https://youtu.be/k4y0ZzYw9Yw?si=O4ET1u-CsUF25ma3')
type(img)  # qrcode.image.pil.PilImage
# here image is saved as given name in brackets
img.save("jitubhaikirasoi.png")
