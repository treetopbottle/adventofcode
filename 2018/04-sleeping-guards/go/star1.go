package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("input")
	lines := strings.Split(string(bytes), "\n")
	lines = lines[:len(lines)-1]
	sort.Strings(lines)

	var year, month, day, hour int // only used for correct parsing
	var guard, minute, sleepStart int
	sleepMinutes := make(map[int][]int)
	for _, line := range lines {
		fmt.Sscanf(line, "[%d-%d-%d %d:%d]", &year, &month, &day, &hour, &minute)
		action := line[19:]

		switch {
		case action[0:1] == "G":
			fmt.Sscanf(action, "Guard #%d begins shift", &guard)
		case action == "falls asleep":
			sleepStart = minute
		case action == "wakes up":
			for i := sleepStart; i < minute; i++ {
				sleepMinutes[guard] = append(sleepMinutes[guard], i)
			}
		}
	}

	var sleepiestGuard, sleepTime int
	for guard, minutes := range sleepMinutes {
		if len(minutes) > sleepTime {
			sleepiestGuard = guard
			sleepTime = len(minutes)
		}
	}

	minuteSlept := make(map[int]int)
	for _, minute := range sleepMinutes[sleepiestGuard] {
		minuteSlept[minute] += 1
	}

	var sleepiestMinute, max int
	for minute, times := range minuteSlept {
		if times > max {
			max = times
			sleepiestMinute = minute
		}
	}
	fmt.Println(sleepiestGuard * sleepiestMinute)
}
