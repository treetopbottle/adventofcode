package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func loopInput(channel chan int) {
	lines, _ := ioutil.ReadFile("input")
	changes := strings.Split(string(lines[0:len(lines)-1]), "\n")

	for {
		for _, change := range changes {
			change, _ := strconv.Atoi(change)
			channel <- change
		}
	}
}

func main() {
	changesLoop := make(chan int, 2)
	go loopInput(changesLoop)

	frequency := 0
	seenFrequencies := map[int]int{frequency: 1}
	for {
		change := <-changesLoop
		frequency += change
		seenFrequencies[frequency] += 1
		if seenFrequencies[frequency] == 2 {
			fmt.Println(frequency)
			break
		}
	}
}
