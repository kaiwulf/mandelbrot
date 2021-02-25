import std.stdio, std.complex;

void mandelbrot(real c_re, real c_im) {
    auto z = complex(0, 0);
    immutable c = complex(c_re, c_im);
    immutable MAX_ITER = 1000;
    foreach(_; 0 .. MAX_ITER ) {
        z = z^^2 + c;
    }
    write(abs(z) < 2 ? '#' : '.');
}

void main() {
    // Image size (pixels)
    immutable WIDTH = 1.0;
    immutable HEIGHT = 1.0;

    // Plot window
    immutable RE_START = -2;
    immutable RE_END = 1;
    immutable IM_START = -1;
    immutable IM_END = 1;

    for(real y = -1.2; y < HEIGHT; y += 0.05) {
        for(real x = -2.5; x < WIDTH; x += 0.03) {
            mandelbrot(x, y);
            
        }
        writeln;
    }
}