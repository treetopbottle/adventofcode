use std::collections::HashSet;

const INPUT: &str = include_str!("../input");

fn main() {
    let mut frequency = 0;
    let mut seen_frequencies = HashSet::new();

    'outer: loop {
        for change in INPUT.lines().map(|s| s.parse::<i32>().unwrap()) {
            frequency += change;
            if !seen_frequencies.insert(frequency) {
                println!("{}", frequency);
                break 'outer;
            }
        }
    }
}
