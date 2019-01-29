use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn parse_line(line: &str) -> (u32, u32, u32, u32, u32) {
    let splitted: Vec<&str> = line
        .split(|c| c == ' ' || c == ',' || c == ':' || c == 'x' || c == '#')
        .collect();

    let id: u32 = splitted[1].parse().unwrap();
    let x: u32 = splitted[3].parse().unwrap();
    let y: u32 = splitted[4].parse().unwrap();
    let w: u32 = splitted[6].parse().unwrap();
    let h: u32 = splitted[7].parse().unwrap();

    return (id, x, y, w, h);
}

fn main() {
    let mut fabric_claims: HashMap<(u32, u32), u32> = HashMap::new();

    for line in INPUT.lines() {
        let (_id, x, y, w, h) = parse_line(line);

        for i in x..x + w {
            for j in y..y + h {
                fabric_claims
                    .entry((i, j))
                    .and_modify(|n| *n += 1)
                    .or_insert(1);
            }
        }
    }

    for line in INPUT.lines() {
        let (id, x, y, w, h) = parse_line(line);

        let mut no_overlap = true;
        for i in x..x + w {
            for j in y..y + h {
                no_overlap = no_overlap && *fabric_claims.get(&(i, j)).unwrap() == 1;
            }
        }

        if no_overlap {
            println!("{}", id);
            break;
        }
    }
}
