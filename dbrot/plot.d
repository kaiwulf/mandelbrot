void main() {
    // Image size (pixels)
    immutable WIDTH = 600;
    immutable HEIGHT = 400;

    // Plot window
    immutable RE_START = -2;
    immutable RE_END = 1;
    immutable IM_START = -1;
    immutable IM_END = 1;

    for(real x = 0.0; x < WIDTH; x += 0.1) {
        for(real y = 0.0; x < HEIGHT; y += 0.1) {
            auto c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START));
            auto m = mandelbrot(c.re, c.im);
            
        }
        writeln
    }
}