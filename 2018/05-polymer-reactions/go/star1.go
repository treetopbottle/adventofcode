package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

func main() {
	input, _ := ioutil.ReadFile("input")
	polymer := strings.TrimSpace(string(input))

	var stack []rune
	for _, unit := range polymer {
		var previous rune
		if len(stack) > 0 {
			previous = stack[len(stack)-1]
		}

		// If same letter, different case
		charDiff := math.Abs(float64(unit - previous))
		if charDiff == 32.0 {
			// Pop previous
			stack = stack[:len(stack)-1]
			continue
		}

		stack = append(stack, unit)
	}

	fmt.Println(len(stack))
}
