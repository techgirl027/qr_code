import qrcode
import random
import string


def function(l=10):
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(l))


def qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img


def save_qr_code(img, filename):
    img.save(filename)


link = "https://najottalim.uz/" + function(10)
file = function(10) + ".png"

qr_img = qr_code(link)

save_qr_code(qr_img, file)

print(f"Link: {link}")
print(f"QR code: {file}")
