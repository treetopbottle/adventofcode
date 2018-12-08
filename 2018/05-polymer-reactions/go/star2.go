package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

const caseDifference = 32

func react(polymer string) string {
	var stack []rune
	for _, unit := range polymer {
		var previous rune
		if len(stack) > 0 {
			previous = stack[len(stack)-1]
		}

		charDiff := math.Abs(float64(unit - previous))
		if charDiff == caseDifference {
			// Pop previous
			stack = stack[:len(stack)-1]
			continue
		}

		stack = append(stack, unit)
	}

	return string(stack)
}

func improve(polymer string, char rune) string {
	upperChar := char - caseDifference

	improved := polymer
	improved = strings.Replace(improved, string(char), "", -1)
	improved = strings.Replace(improved, string(upperChar), "", -1)

	return improved
}

func main() {
	input, _ := ioutil.ReadFile("input")
	polymer := strings.TrimSpace(string(input))

	minLength := 99999.0
	for _, char := range "qwertyuiopasdfghjklzxcvbnm" {
		improvedPolymer := improve(polymer, char)
		length := len(react(improvedPolymer))
		minLength = math.Min(minLength, float64(length))
	}
	fmt.Println(minLength)
}
