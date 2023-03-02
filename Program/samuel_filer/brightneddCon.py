from PIL import Image, ImageEnhance

path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/skyteskive.jpg"

img = Image.open(path).convert("RGB")

img_enhancer = ImageEnhance.Brightness(img)

factor = 1
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.save("output/original-image.png")

factor = 0.5
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.save("output/dark-image.png")

factor = 1.5
enhanced_output = img_enhancer.enhance(factor)
enhanced_output.save("output/bright-image.png")