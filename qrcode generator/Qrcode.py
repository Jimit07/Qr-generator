# create a qr code image for your link

import qrcode as qr
img = qr.make('https://youtu.be/k4y0ZzYw9Yw?si=O4ET1u-CsUF25ma3')
type(img)  # qrcode.image.pil.PilImage
img.save("jitubhaikirasoi.png")