package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

const maxDistance = 10000

type point struct {
	x int
	y int
}

func absInt(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func distance(p1, p2 point) int {
	return absInt(p1.x-p2.x) + absInt(p1.y-p2.y)
}

func main() {
	bytes, _ := ioutil.ReadFile("input")
	lines := strings.Split(string(bytes), "\n")

	topLeft := point{math.MaxInt32, math.MaxInt32}
	bottomRight := point{math.MinInt32, math.MinInt32}

	var coords []point
	for _, line := range lines {
		if line == "" {
			continue
		}

		var x, y int
		fmt.Sscanf(line, "%d, %d", &x, &y)
		coords = append(coords, point{x, y})

		topLeft = point{minInt(topLeft.x, x), minInt(topLeft.y, y)}
		bottomRight = point{maxInt(bottomRight.x, x), maxInt(bottomRight.y, y)}
	}

	nrInRegion := 0
	for x := topLeft.x + 1; x < bottomRight.x-1; x++ {
		for y := topLeft.y + 1; y < bottomRight.y-1; y++ {
			totalDistance := 0
			for _, coord := range coords {
				totalDistance += distance(coord, point{x, y})
			}

			if totalDistance < maxDistance {
				nrInRegion += 1
			}
		}
	}

	fmt.Println(nrInRegion)
}
