use.std

// Image size (pixels)
immutable WIDTH = 600
immutable HEIGHT = 400

// Plot window
immutable RE_START = -2
immutable RE_END = 1
immutable IM_START = -1
immutable IM_END = 1

foreach(x; 0 .. WIDTH) {
    foreach(y; 0 .. HEIGHT) {
        auto c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        auto m = mandelbrot(c.re, c.im)
    }
}