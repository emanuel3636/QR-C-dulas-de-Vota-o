import qrcode
import random
from PIL import Image 

def qrcode_hash():
    for i in range(0,500):
        hash = random.getrandbits(128)

        print(str(i) + "Valor Hash: %032x" % hash)

        input_data = "Valor Hash: %032x" % hash

        qr = qrcode.QRCode(
                version=1,
                box_size=3,
                border=4)

        qr.add_data(input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode00'+str(i)+'.png')

        img1 = Image.open(r"cedula.png") 
        img2 = Image.open(r"qrcode00"+str(i)+".png") 
        img1.paste(img2, (0,0))
        img1.save('qrcode00'+str(i)+'.png')


    
    

qrcode_hash()
  

