package main

import (
    "io/ioutil"
    "fmt"
    "strings"
)

func main() {
    bytes, _ := ioutil.ReadFile("input")
    lines := strings.Split(string(bytes), "\n")

    claimedSquares := make(map[[2]int]int)
    for _, line := range lines {
        if line == "" {
            continue
        }
        var id, x, y, w, h int
        fmt.Sscanf(line, "#%d @ %d,%d: %dx%d", &id, &x, &y, &w, &h)

        for i := x; i < x+w; i++ {
            for j := y; j < y+h; j++ {
                claimedSquares[[2]int{i, j}] += 1
            }
        }
    }

    doubleClaims := 0
    for _, claims := range claimedSquares {
        if claims > 1 {
            doubleClaims += 1
        }
    }

    fmt.Println(doubleClaims)
}
