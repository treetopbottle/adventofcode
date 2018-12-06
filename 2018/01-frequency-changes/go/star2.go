package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func findDoubleFrequency(start int, changes []string) int {
    frequency := start
    seenFrequencies := []int{frequency}
    for {
        for _, change := range changes {
            change, _ := strconv.Atoi(change)
            frequency += change
            for _, seenFrequency := range seenFrequencies {
                if frequency == seenFrequency {
                    return frequency
                }
            }
            seenFrequencies = append(seenFrequencies, frequency)
        }
    }
}

func main() {
    lines, _ := ioutil.ReadFile("input")
    changes := strings.Split(string(lines[0:len(lines)-1]), "\n")

    doubleFrequency := findDoubleFrequency(0, changes)
    fmt.Println(doubleFrequency)
}
