import matplotlib.pyplot as plt
import numpy as np

# Generate dataset for the plot
x = np.linspace(-10, 10, 1000)
y = np.sin(x)

# Plot the data
plt.plot(x, y, color='red')

# Use the rdbu colormap to color the background
plt.imshow(np.outer(np.ones(10), np.arange(100)),
           cmap='RdBu',
           extent=(-10, 10, -1, 1),
           alpha=0.2)

# Add text to the plot using an rgba color
plt.text(5, 0.5, 'Text in RGBA color', color=(0, 1, 0, 0.5), fontsize=16)

# Show the plot
plt.show()