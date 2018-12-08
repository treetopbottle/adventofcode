package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	lines, _ := ioutil.ReadFile("input")
	boxIds := []string{}
	for _, line := range bytes.Split(lines, []byte{'\n'}) {
		if len(line) > 0 {
			boxIds = append(boxIds, string(line))
		}
	}

	numberTwos := 0
	numberThrees := 0

	for _, boxId := range boxIds {
		twoFound := false
		threeFound := false

		for _, char := range boxId {
			if strings.Count(boxId, string(char)) == 2 {
				twoFound = true
			}
			if strings.Count(boxId, string(char)) == 3 {
				threeFound = true
			}
		}

		if twoFound {
			numberTwos += 1
		}
		if threeFound {
			numberThrees += 1
		}
	}

	fmt.Println(numberTwos * numberThrees)
}
