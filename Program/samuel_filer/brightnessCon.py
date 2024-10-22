from PIL import Image, ImageEnhance
import cv2 as cv

path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/skyteskive.jpg"
img = Image.open(path).convert("RGB")



img_enhancer = ImageEnhance.Brightness(img)

factor = 1
enhanced_output = img_enhancer.enhance(factor)

enhanced_output.save("C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/original-image.png")

factor = 0.5
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.save("C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/dark-image.png")

factor = 2
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.save("C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/bright-image.png")


