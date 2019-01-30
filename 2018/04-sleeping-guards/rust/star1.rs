use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn parse(line: &str) -> (&str, u32) {
    let splitted: Vec<&str> = line.split(']').collect();
    let action = &splitted[1][1..];
    let minute: u32 = splitted[0][15..].parse().unwrap();
    return (&action, minute);
}

fn measure_sleep_times(
    sorted_lines: Vec<&str>,
) -> (HashMap<u32, u32>, HashMap<u32, HashMap<u32, u32>>) {
    let mut guard_sleep_time: HashMap<u32, u32> = HashMap::new();
    let mut guard_minute_asleep: HashMap<u32, HashMap<u32, u32>> = HashMap::new();
    let mut current_guard = 0;
    let mut sleep_start = 0;

    for line in sorted_lines {
        let (action, minute) = parse(line);
        if action.starts_with("Guard #") {
            current_guard = action.split(' ').nth(1).unwrap()[1..].parse().unwrap();
        } else if action == "falls asleep" {
            sleep_start = minute;
        } else if action == "wakes up" {
            let sleep_time = minute - sleep_start;
            *guard_sleep_time.entry(current_guard).or_default() += sleep_time;
            for min in sleep_start..minute {
                *guard_minute_asleep
                    .entry(current_guard)
                    .or_default()
                    .entry(min)
                    .or_default() += 1;
            }
        }
    }

    return (guard_sleep_time, guard_minute_asleep);
}

fn main() {
    let mut lines: Vec<&str> = INPUT.lines().collect();
    lines.sort();

    let (guard_sleep_time, guard_minute_asleep) = measure_sleep_times(lines);

    let mut sleepiest_guard: (&u32, &u32) = (&0, &0);
    for guard in guard_sleep_time.iter() {
        if guard.1 > sleepiest_guard.1 {
            sleepiest_guard = guard;
        }
    }
    let sleepiest_guard = sleepiest_guard.0;

    let mut sleepiest_minute: (&u32, &u32) = (&0, &0);
    for minute in guard_minute_asleep.get(sleepiest_guard).unwrap().iter() {
        if minute.1 > sleepiest_minute.1 {
            sleepiest_minute = minute;
        }
    }
    let sleepiest_minute = sleepiest_minute.0;

    println!("{:?}", sleepiest_guard * sleepiest_minute);
}
