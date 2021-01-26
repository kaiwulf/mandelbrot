class pixel(x, y):
    self.affix = x
    self.color = y

def mod_z2(z):
    x = z[0]
    y = z[1]

    mod = x**2 + y**2
    return mod

def mult_z(z):
    x = z[0]
    y = z[1]

    z[0] = x**2 - y**2
    z[1] = 2*x*y

def add_z_c(z,c):
    z[0] = z[0] + c[0]
    z[1] = z[1] + c[1]
    return z

def main():
    z = []
    N = 20
    itMax = 200
    
    for p in zip(range(1,N),range(1,N)):
        p = pixel([0,0],' ')
        c = p.affix # I'm not properly understanding this part
        z = [0,0]
        
        
        
        for iter in range(0,itMax):
            if 
        z = mult_z(z)
        z = add_z_c(z,c)
    p.color = color



if __name__ == "__main__":
    main()
