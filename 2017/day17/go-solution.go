package main

import (
    "fmt"
)

func main() {
    step_size := 312
    nr_steps := 50000000

    cur_index := 0
    number_after_zero := 0
    for num := 1; num < nr_steps+1; num++ {
        cur_index = ((cur_index + step_size) % num) + 1

        if cur_index == 1 {
            number_after_zero = num
        }
    }

    fmt.Printf("%d\n", number_after_zero)

}
