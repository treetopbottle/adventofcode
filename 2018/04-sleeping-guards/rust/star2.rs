use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn parse(line: &str) -> (&str, u32) {
    let splitted: Vec<&str> = line.split(']').collect();
    let action = &splitted[1][1..];
    let minute: u32 = splitted[0][15..].parse().unwrap();
    return (&action, minute);
}

fn measure_sleep_times(sorted_lines: Vec<&str>) -> HashMap<(u32, u32), u32> {
    let mut guard_minute_sleep_time: HashMap<(u32, u32), u32> = HashMap::new();

    let mut current_guard = 0;
    let mut sleep_start = 0;
    for line in sorted_lines {
        let (action, minute) = parse(line);
        if action.starts_with("Guard #") {
            current_guard = action.split(' ').nth(1).unwrap()[1..].parse().unwrap();
        } else if action == "falls asleep" {
            sleep_start = minute;
        } else if action == "wakes up" {
            for min in sleep_start..minute {
                *guard_minute_sleep_time
                    .entry((current_guard, min))
                    .or_default() += 1;
            }
        }
    }

    return guard_minute_sleep_time;
}

fn main() {
    let mut lines: Vec<&str> = INPUT.lines().collect();
    lines.sort();

    let guard_minute_sleep_time = measure_sleep_times(lines);

    let mut sleepiest_guard_minute: (&(u32, u32), &u32) = (&(0, 0), &0);
    for guard_minute in guard_minute_sleep_time.iter() {
        if guard_minute.1 > sleepiest_guard_minute.1 {
            sleepiest_guard_minute = guard_minute;
        }
    }
    let sleepiest_guard_minute = sleepiest_guard_minute.0;

    println!("{:?}", sleepiest_guard_minute.0 * sleepiest_guard_minute.1);
}
