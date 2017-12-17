package main

import (
    "fmt"
)

func main() {
    const step_size = 312
    const nr_steps = 2017

    var buf [nr_steps+1]int
    cur_index := 0
    for num := 1; num < nr_steps+1; num++ {
        cur_index = ((cur_index + step_size) % num) + 1

        for i := num; i > cur_index; i-- {
            buf[i] = buf[i-1]
        }
        buf[cur_index] = num
    }

    for i, num := range buf {
        if num == 2017 {
            fmt.Println(buf[i+1])
            break
        }
    }
}
