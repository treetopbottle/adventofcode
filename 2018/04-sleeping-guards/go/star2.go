package main

import (
    "io/ioutil"
    "fmt"
    "strings"
    "sort"
)

func main() {
    bytes, _ := ioutil.ReadFile("input")
    lines := strings.Split(string(bytes), "\n")
    lines = lines[:len(lines)-1]
    sort.Strings(lines)

    var year, month, day, hour int // only used for correct parsing
    var guard, minute, sleepStart int
    minutesSlept := make(map[[2]int]int)
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
                    guardMinute := [2]int{guard, i}
                    minutesSlept[guardMinute] += 1
                }
        }
    }

    var sleepTime int
    var sleepiest [2]int
    for guardMinute, minutes := range minutesSlept {
        if minutes > sleepTime {
            sleepiest = guardMinute
            sleepTime = minutes
        }
    }

    fmt.Println(sleepiest[0] * sleepiest[1])
}

