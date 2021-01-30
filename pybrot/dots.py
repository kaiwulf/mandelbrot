dots = open("dots.ppm", "w")
width = 800
height = 800
maxval = 255
ppm_header = 'P3 {width} {height} {maxval}\n'
i,j,k = 0,0,0
color = [0,0,0]
color[0],color[1],color[2]=i,j,k
for p in range(1,800):
    i+=1
    for q in range(1,800):
        color[0],color[1],color[2] = i,j,k
        j+=1
        if q%2:
            k+=1
        dots.write("{} ".format(color[0]))
        dots.write("{} ".format(color[1]))
        dots.write("{} ".format(color[2]))
        if i == 255 or j == 255 or k == 255:
            i=0
            j=0
            k=0
            break
    dots.write("\n")
