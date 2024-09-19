from PIL import Image
import matplotlib.pyplot as plt



# Mở file PGM
img = Image.open("2.pgm")

# Hiển thị ảnh
plt.imshow(img, cmap='gray')
plt.show()
