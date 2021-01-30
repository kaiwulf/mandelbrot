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
    dims = 100              # Set the pixel dimensions (dims x dims)
    itMax = 200         # Max iterations of mendelbrot set

    CxMin = -2.5
    CxMax = 1.5

    CyMin = -2.0
    CyMax = 2.0
    
    it = 0

    PixelHeight = (CyMax - CyMin)/dims
    PixelWidth = (CxMax - CxMin)/dims

    mendlppm = open("mendel.ppm")

                                            # Iteration through the square (1,dims)x(1,dims) - Cartesian product
    for p in range(1,dims):
        c[0] = p
        # if abs(c[1] < PixelHeight/2):
        #     c[1] = 0
        
        z = [0,0]                           # For each unit...
        for q in range(1,dims):
            c[1] = q
                                            # Calculate that max iterations...
            for it in range(0,itMax):
                if mod_z2(z) < 4.0:
                    z = mult_z(z)
                    z = add_z_c(z,c)
                    break

            if it == itMax:
                print(" ", end="")
            else: 
                print("*", end="")
        print("\n")


if __name__ == "__main__":
    main()
