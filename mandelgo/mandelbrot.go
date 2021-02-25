package main

import  ( "fmt"
          "math/cmplx" )

func mandelbrot(c_re float64, c_im float64) {
    var z complex128 = 0+0i
    var c complex128 = complex(c_re, c_im)

    MAX_ITER := 80
    for i := 0; i < MAX_ITER; i++ {
        z = z*z + c
    }
    if cmplx.Abs(z) < 2 {
        fmt.Printf("#")
    } else {
        fmt.Printf(".")
    }
}

func main() {

    var height float64 = 1.0
    var width float64 = 1.0

    for y := -1.2; y < height; y += 0.05 {
        for x := -2.5; x < width; x += 0.03 {
            mandelbrot(x, y)
        }
        fmt.Printf("\n")
    }


}