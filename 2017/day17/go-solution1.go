package main

import (
    "fmt"
)

func main() {
    const step_size = 312
    const nr_steps = 2017

    buf := []int{0}
    cur_index := 0
    for num := 1; num < nr_steps+1; num++ {
        cur_index = ((cur_index + step_size) % num) + 1

        before := buf[:cur_index]
        after := append([]int{num}, buf[cur_index:]...)
        buf = append(before, after...)
    }

    for i, num := range buf {
        if num == 2017 {
            fmt.Println(buf[i+1])
            break
        }
    }
}
