package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

func distance(p1 [2]int, p2 [2]int) int {
	return int(math.Abs(float64(p1[0])-float64(p2[0])) +
		math.Abs(float64(p1[1])-float64(p2[1])))
}

func main() {
	bytes, _ := ioutil.ReadFile("input")
	lines := strings.Split(string(bytes), "\n")

	// Boundaries to determine non-infinite areas
	minX := 99999
	minY := 99999
	maxX := 0
	maxY := 0

	var coords [][2]int

	for _, line := range lines {
		if line == "" {
			continue
		}

		var x, y int
		fmt.Sscanf(line, "%d, %d", &x, &y)
		coords = append(coords, [2]int{x, y})

		minX = int(math.Min(float64(minX), float64(x)))
		minY = int(math.Min(float64(minY), float64(y)))
		maxX = int(math.Max(float64(maxX), float64(x)))
		maxY = int(math.Max(float64(maxY), float64(y)))
	}

	areas := make(map[[2]int]int)
	maxArea := 0
	for i := minX + 1; i < maxX; i++ {
		for j := minY + 1; j < maxY; j++ {
			closestDist := 99999
			var closest [2]int
			var onlyOne bool

			for _, coord := range coords {
				dist := distance(coord, [2]int{i, j})
				if dist < closestDist {
					closest = coord
					closestDist = dist
					onlyOne = true
				} else if dist == closestDist {
					onlyOne = false
				}
			}

			if onlyOne {
				withinX := closest[0] > minX && closest[0] < maxX
				withinY := closest[1] > minY && closest[1] < maxY
				if withinX && withinY {
					areas[closest] += 1
					maxArea = int(math.Max(float64(maxArea), float64(areas[closest])))
				}
			}
		}
	}

	fmt.Println(maxArea)
}
