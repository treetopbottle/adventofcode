use std::cmp::min;

const INPUT: &str = include_str!("../input");

fn reacts(c1: char, c2: char) -> bool {
    return (c1 != c2) && (c1.to_uppercase().to_string() == c2.to_uppercase().to_string());
}

fn fully_react(polymer: &str, remove: char) -> usize {
    let mut stack = Vec::new();
    for c in polymer.chars() {
        if c.to_uppercase().to_string() == remove.to_uppercase().to_string() {
            continue;
        }

        if stack.is_empty() {
            stack.push(c);
            continue;
        }

        if reacts(c, stack[stack.len() - 1]) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }

    stack.len()
}

fn main() {
    let polymer = INPUT.trim();

    let mut min_length = 1_000_000;
    for c in "qwertyuiopasdfghjklzxcvbnm".chars() {
        min_length = min(min_length, fully_react(polymer, c));
    }

    println!("{}", min_length);
}
