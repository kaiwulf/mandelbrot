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

# Add z and c together
def add_z_c(z,c):
    z_add = [0,0]
    z_add[0] = z[0] + c[0]
    z_add[1] = z[1] + c[1]
    return z_add

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

    for p in zip(range(1,N),range(1,N)):    # Iteration through the square (1,N)x(1,N) - Cartesian product
        c[0] = CyMin + p[1]*PixelHeight
        c[1] = CxMin + p[0]*PixelWidth
        if abs(c[1] < PixelHeight/2):
            c[1] = 0
        
        z = [0,0]                           # For each unit...
        for iter in range(0,itMax):         # Calculate that max iterations
            if mod_z2(z) < 4:
                print("c is ", c)
                print("z is ", z)
                z = mult_z(z)
                z = add_z_c(z,c)
                break
        
        if iter == itMax:
            print(" ")
        else: 
            print("*")


if __name__ == "__main__":
    main()
