package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func main() {
    lines, _ := ioutil.ReadFile("input")
    stringNumbers := strings.Split(string(lines), "\n")

    frequency := 0
    for _, stringNumber := range stringNumbers {
        number, _ := strconv.Atoi(stringNumber)
        frequency += number
    }

    fmt.Println(frequency)
}
