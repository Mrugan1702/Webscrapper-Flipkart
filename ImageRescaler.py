import PIL
from PIL import Image
imp = input("Specify Path of you image:\n")
image1 = Image.open(imp)
quality = input("Enter a value between 1 to 95 for your choice of resolution of image:\n")
quality = int(quality)
image1.save("quality.jpg", resolution=quality)
