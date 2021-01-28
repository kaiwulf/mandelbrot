# class pixel(x, y):
#     self.affix = x
#     self.color = y

# Modulus of z
def mod_z2(z):
    x = z[0]
    y = z[1]

    mod = x**2 + y**2
    return mod

# Multiply z by itself
def mult_z(z):
    x = z[0]
    y = z[1]

    z[0] = x**2 - y**2
    z[1] = 2*x*y
    return z

# Add z and c together
def add_z_c(z,c):
    z[0] = z[0] + c[0]
    z[1] = z[1] + c[1]

    return z

def main():
    z = [0,0]              # Create a list z
    c = [0,0]              # Create a list c
    N = 20              # Set the size of units (rather than pixels) to N
    itMax = 200         # Max iterations of mendelbrot set

    CxMin = -2.5
    CxMax = 1.5

    CyMin = -2.0
    CyMax = 2.0

    PixelHeight = (CyMax - CyMin)/N
    PixelWidth = (CxMax - CxMin)/N

                                            # Iteration through the square (1,N)x(1,N) - Cartesian product
    for p in zip(range(1,N),range(1,N)):
        c[0] = CyMin + p[1]*PixelHeight
        c[1] = CxMin + p[0]*PixelWidth
        if abs(c[1] < PixelHeight/2):
            c[1] = 0
        
        z = [0,0]                           # For each unit...
                                            # Calculate that max iterations...
        for iter in range(0,itMax):
            if mod_z2(z) < 4.0:
                z = mult_z(z)
                z = add_z_c(z,c)
                break
        
        if iter == itMax:
            print(" ")
        else: 
            print("*")


if __name__ == "__main__":
    main()
