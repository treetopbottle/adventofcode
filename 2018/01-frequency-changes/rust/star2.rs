use std::collections::HashSet;

fn main() {
    let input = include_str!("../input");

    let mut frequency = 0;
    let mut seen_frequencies = HashSet::new();
    'outer: loop {
        for line in input.lines() {
            let change = line.parse::<i32>().unwrap();
            frequency += change;
            if seen_frequencies.contains(&frequency) {
                println!("{}", frequency);
                break 'outer;
            }
            seen_frequencies.insert(frequency);
        }
    }
}
