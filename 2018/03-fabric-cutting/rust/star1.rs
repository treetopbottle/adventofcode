use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn parse_line(line: &str) -> (u32, u32, u32, u32) {
    let splitted: Vec<&str> = line
        .split(|c| c == ' ' || c == ',' || c == ':' || c == 'x')
        .collect();

    let x: u32 = splitted[2].parse().unwrap();
    let y: u32 = splitted[3].parse().unwrap();
    let w: u32 = splitted[5].parse().unwrap();
    let h: u32 = splitted[6].parse().unwrap();

    return (x, y, w, h);
}

fn main() {
    let mut fabric_claims: HashMap<(u32, u32), u32> = HashMap::new();

    for line in INPUT.lines() {
        let (x, y, w, h) = parse_line(line);

        for i in x..x + w {
            for j in y..y + h {
                fabric_claims
                    .entry((i, j))
                    .and_modify(|n| *n += 1)
                    .or_insert(1);
            }
        }
    }

    let len = fabric_claims.values().filter(|v| **v > 1).count();
    println!("{}", len);
}
