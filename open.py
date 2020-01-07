import PIL

from PIL import Image
img = Image.open("C:\\Users\\Yp\\Pictures\\egg.png").convert('L')
WIDTH, HEIGHT = img.size

data = list(img.getdata())
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

for row in data:
    print(' '.join('{:3}'.format(value) for value in row))