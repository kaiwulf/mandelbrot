import std.complex, std.stdio;
//module mandelbrot;


void mandelbrot(real c_re, real c_im) {
    auto z = complex(0, 0);
    immutable c = complex(c_re, c_im);
    uint n = 0;
    immutable MAX_ITER = 80;
    immutable zabs = abs(z);
    while(zabs <= 2 && n < MAX_ITER ) {
     z = z*z + c;
     n += 1;
    }
    write(zabs < 2 ? '#' : '.');

    //return n;
}

//void main() {
   
////    write(complex(1,1), " ", mandelbrot(1,1));

//    for(real i = -10.0; i <= 10.0; i += 1) {
//        for(real j = -10.0; j <= 10.0; j += 1) {
//            auto c = complex(i / 10, j / 10);
//            write(c, " ", mandelbrot(c.re, c.im), "\n");
//        }
//    }
//}