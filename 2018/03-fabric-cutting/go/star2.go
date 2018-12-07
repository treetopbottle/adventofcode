package main

import (
    "io/ioutil"
    "fmt"
    "strings"
)

func main() {
    bytes, _ := ioutil.ReadFile("input")
    lines := strings.Split(string(bytes), "\n")

    claims := make(map[int][4]int)
    claimedSquares := make(map[[2]int]int)
    for _, line := range lines {
        if line == "" {
            continue
        }
        var id, x, y, w, h int
        fmt.Sscanf(line, "#%d @ %d,%d: %dx%d", &id, &x, &y, &w, &h)

        claims[id] = [4]int{x, y, w, h}

        for i := x; i < x+w; i++ {
            for j := y; j < y+h; j++ {
                coord := [2]int{i, j}
                claimedSquares[coord] += 1
            }
        }
    }

    for id, claim := range claims {
        x := claim[0]
        y := claim[1]
        w := claim[2]
        h := claim[3]

        overlaps := false
        for i := x; i < x+w; i++ {
            for j := y; j < y+h; j++ {
                coord := [2]int{i, j}
                if claimedSquares[coord] > 1 {
                    overlaps = true
                }
            }
        }

        if !overlaps {
            fmt.Println(id)
        }
    }
}
