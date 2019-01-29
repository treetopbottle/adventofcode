use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn main() {
    let mut nr2 = 0;
    let mut nr3 = 0;

    for box_id in INPUT.lines() {
        let mut char_occurences = HashMap::new();
        for c in box_id.chars() {
            char_occurences
                .entry(c)
                .and_modify(|n| *n += 1)
                .or_insert(1);
        }

        let mut has2 = false;
        let mut has3 = false;
        for k in char_occurences.values() {
            if *k == 2 {
                has2 = true;
            }

            if *k == 3 {
                has3 = true;
            }
        }

        if has2 {
            nr2 += 1;
        }

        if has3 {
            nr3 += 1;
        }
    }

    println!("{}", nr2 * nr3);
}
