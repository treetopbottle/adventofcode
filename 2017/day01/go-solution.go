package main

import (
    "fmt"
    "io/ioutil"
    "strings"
)

func main() {

    dat, _ := ioutil.ReadFile("./input1")

    numbers := strings.Replace(string(dat), "\n", "", 1)
    sum := 0

    for i, _ := range numbers {
        //j := (i+1) % len(numbers)
        j := (i + len(numbers)/2) % len(numbers)

        if numbers[i] == numbers[j] {
            sum += int(numbers[i] - '0')
        }
    }

    fmt.Printf("%d", sum)

}
