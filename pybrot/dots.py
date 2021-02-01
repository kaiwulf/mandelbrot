import array
width = 800
height = 800
maxval = 255

r = 255
g = 255
b = 255

ppm_header = f'P6 {width} {height} {maxval}\n'

image = array.array('B', [r, g, b] * width * height)

for y in range(10,90):
    for x in range(10,60):
        index = 3*(y*width + x)
        image[index] = 255
        image[index+1] = 0
        image[index+2] = 0

with open('dots.ppm', 'wb') as dots:
    dots.write(bytearray(ppm_header, 'ascii'))
    image.tofile(dots)
