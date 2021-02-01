import array

# Modulus of z
def mod_z2(z):
    x = z[0]
    y = z[1]

    mod = x**2 + y**2
    return mod

# Multiply z by itself
def mult_z(z, c):
    x = z[0]
    y = z[1]

    z[0] = x**2 - y**2 + c[0]
    z[1] = 2*x*y + c[1]
    return z

# Add z and c together
def add_z_c(z,c):
    z[0] = z[0] + c[0]
    z[1] = z[1] + c[1]

    return z

def main():
    width = 800
    height = 800
    maxval = 255

    r = 255
    g = 255
    b = 255

    ppm_header = f'P6 {width} {height} {maxval}\n'

    image = array.array('B', [r, g, b] * width * height)

    z = [0,0]              # Create a list z
    c = [0,0]              # Create a list c
    cX = 0
    cY = 0
    dims = 100              # Set the pixel dimensions (dims x dims)
    itMax = 200         # Max iterations of mendelbrot set

    CxMin = -2.5
    CxMax = 1.5

    CyMin = -2.0
    CyMax = 2.0
    
    it = 0

    PixelHeight = (CyMax - CyMin)/dims
    PixelWidth = (CxMax - CxMin)/dims

    for p in range(0,dims):
        cY = CyMin + p*PixelHeight
        if abs(cY < PixelHeight/2):
            cY = 0
        
        z = [0,0]
        z[0] = z[0]*z[0]
        z[1] = z[1]*z[1]
        for q in range(0,dims):
            cX = CxMin + q*PixelWidth
            c[0],c[1] = cX,cY
            # print(c)
            for it in range(0,itMax):
                if mod_z2(z) >= 4.0:
                    break
                z = mult_z(z,c)
                # input(z)
                # z = add_z_c(z,c)
                z[0] = z[0]*z[0]
                z[1] = z[1]*z[1]
                # input(z)

            if it == itMax:
               index = 3*(p*width + q)
               image[index] = 0
               image[index+1] = 0
               image[index+2] = 0
    
    with open('dots.ppm', 'wb') as mendelppm:
        mendelppm.write(bytearray(ppm_header, 'ascii'))
        image.tofile(mendelppm)


if __name__ == "__main__":
    main()
