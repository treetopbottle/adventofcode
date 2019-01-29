const INPUT: &str = include_str!("../input");

fn main() {
    'outer: for id1 in INPUT.lines() {
        for id2 in INPUT.lines() {
            let mut different_chars = 0;
            // Direct indexing in a string isn't supported, so loop over both
            for (i, c1) in id1.char_indices() {
                for (j, c2) in id2.char_indices() {
                    if i == j && c1 != c2 {
                        different_chars += 1
                    }
                }
            }

            if different_chars == 1 {
                // Print the matching characters
                for (i, c1) in id1.char_indices() {
                    for (j, c2) in id2.char_indices() {
                        if i == j && c1 == c2 {
                            print!("{}", c1);
                        }
                    }
                }
                println!();
                break 'outer;
            }
        }
    }
}
