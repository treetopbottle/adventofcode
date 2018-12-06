package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func findDoubleFrequency(start int, changes []string) int {
    frequency := start
    seenFrequencies := map[int]int{frequency: 1}
    for {
        for _, change := range changes {
            change, _ := strconv.Atoi(change)
            frequency += change
            seenFrequencies[frequency] += 1
            if seenFrequencies[frequency] == 2 {
                return frequency
            }
        }
    }
}

func main() {
    lines, _ := ioutil.ReadFile("input")
    changes := strings.Split(string(lines[0:len(lines)-1]), "\n")

    doubleFrequency := findDoubleFrequency(0, changes)
    fmt.Println(doubleFrequency)
}
