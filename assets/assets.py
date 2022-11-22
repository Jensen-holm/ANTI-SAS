from PIL import Image
import plotille as plt
import os

fp: str = os.getcwd() + "/assets"
anti_sas_logo = "/antisas.png"


def logo():
    img: Image.Image = Image.open(fp + anti_sas_logo)
    # img.convert("rgb")
    img.resize((80, 80))
    cvs = plt.Canvas(80, 80)
    cvs.image(img.getdata())
    print(cvs.plot())
