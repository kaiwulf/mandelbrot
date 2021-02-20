use std.complex

auto mandelbrot(real c_re, real c_im) {
    auto z = complex(0, 0);
    uint n = 0;
    immutable MAX_ITER = 80;
    while(abs(z) <= 2 && n < MAX_ITER ) {
        z = z*z + c;
        n += 1;
    }

    return z;
}