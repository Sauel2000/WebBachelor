import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
'''
# Generate dataset for the plot
x = np.linspace(-5, 5, 25)
y = np.linspace(2, 5, 25)

# Plot the data
plt.plot(x, y, color='red')

# Use the rdbu colormap to color the background

plt.imshow(np.outer(np.ones(2), np.arange(25)),
           cmap='RdBu',
           extent=(-5, 5, -5, 5),
           alpha=0.2)



# Add text to the plot using an rgba color
plt.text(5, 0.5, 'Text in RGBA color', color=(0, 1, 0, 0.5), fontsize=16)

# Show the plot
plt.show()
'''
path = "C:/Users/Samue/Desktop/BachelorGit/WebBachelor/Program/samuel_filer/samuel_bilder/Skyteskive.jpg"
img = cv.imread(path,0)


plt.rcParams["figure.figsize"] = [5, 5]
#plt.rcParams["figure.autolayout"] = True
#d = np.random.rand(8, 8)
plt.imshow(img, origin='upper', extent=[0, 2, 0, 2], aspect=1, cmap='gray')
plt.show()