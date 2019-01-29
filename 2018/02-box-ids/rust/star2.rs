const INPUT: &str = include_str!("../input");

fn main() {
    for id1 in INPUT.lines() {
        for id2 in INPUT.lines() {
            let same_chars: String = id1
                .chars()
                .zip(id2.chars())
                .filter(|(c1, c2)| c1 == c2)
                .map(|(c1, _)| c1)
                .collect();

            if same_chars.len() == id1.len() - 1 {
                println!("{}", same_chars);
            }
        }
    }
}
