const INPUT: &str = include_str!("../input");

fn main() {
    'outer: for id1 in INPUT.lines() {
        for id2 in INPUT.lines() {
            let mut different_chars = 0;
            for (c1, c2) in id1.chars().zip(id2.chars()) {
                if c1 != c2 {
                    different_chars += 1;
                }
            }

            if different_chars == 1 {
                for (c1, c2) in id1.chars().zip(id2.chars()) {
                    if c1 == c2 {
                        print!("{}", c1);
                        different_chars += 1;
                    }
                }
                println!();
                break 'outer;
            }
        }
    }
}
