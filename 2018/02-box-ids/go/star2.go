package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
)

func main() {
	lines, _ := ioutil.ReadFile("input")
	boxIds := []string{}
	for _, line := range bytes.Split(lines, []byte{'\n'}) {
		if len(line) > 0 {
			boxIds = append(boxIds, string(line))
		}
	}

	for _, boxId1 := range boxIds {
		for _, boxId2 := range boxIds {
			differences := 0
			for i := 0; i < len(boxId1); i++ {
				if boxId1[i] != boxId2[i] {
					differences += 1
				}
			}
			if differences == 1 {
				for i := 0; i < len(boxId1); i++ {
					if boxId1[i] == boxId2[i] {
						fmt.Print(string(boxId1[i]))
					}
				}
				fmt.Println()
			}
		}
	}
}
