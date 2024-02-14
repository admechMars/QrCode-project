import qrcode


def make_qrcode(dados):
    img = qrcode.make(dados)
    img_path = f"Qr_Code_{dados}.png"
    img.save(img_path)
    return img_path


