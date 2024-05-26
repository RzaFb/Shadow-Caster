from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("source.jpg")
arr = np.array(im)
image_x = im.size[0]
image_y = im.size[1]

new_image = np.full((image_y * 2, image_x * 2, 3), 254)

for i in range(image_x):
    for j in range(image_y):
        if arr[j][i][0] < 230 or arr[j][i][1] < 230 or arr[j][i][2] < 230:
            new_image[j][int(i) + int(j - image_x * 0.5)][:] = 160

for i in range(image_x):
    for j in range(image_y):
        if (arr[j][i][0] >= 225 and arr[j][i][1] >= 225 and arr[j][i][2] >= 225 and
                new_image[j][i][0] == 160 and new_image[j][i][1] == 160 and new_image[j][i][2] == 160):
            arr[j][i][:] = new_image[j][i][:]

img = Image.fromarray(arr, 'RGB')
plt.imshow(img)
img.save("my.png")
plt.show()
