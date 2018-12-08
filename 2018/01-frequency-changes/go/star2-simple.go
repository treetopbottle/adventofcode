package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	lines, _ := ioutil.ReadFile("input")
	changes := strings.Split(string(lines[0:len(lines)-1]), "\n")

	frequency := 0
	seenFrequencies := map[int]int{frequency: 1}

	doubleFound := false
	for i := 0; !doubleFound; i++ {
		change, _ := strconv.Atoi(changes[i%len(changes)])
		frequency += change
		seenFrequencies[frequency] += 1
		if seenFrequencies[frequency] == 2 {
			fmt.Println(frequency)
			doubleFound = true
		}
	}
}
