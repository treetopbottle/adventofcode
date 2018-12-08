package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

const maxDistance = 10000

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

	nrInRegion := 0
	for i := minX + 1; i < maxX; i++ {
		for j := minY + 1; j < maxY; j++ {
			totalDistance := 0
			for _, coord := range coords {
				dist := distance(coord, [2]int{i, j})
				totalDistance += dist
			}

			if totalDistance < maxDistance {
				nrInRegion += 1
			}
		}
	}

	fmt.Println(nrInRegion)
}
