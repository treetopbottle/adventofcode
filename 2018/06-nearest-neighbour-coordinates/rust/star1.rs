use std::collections::HashMap;

const INPUT: &str = include_str!("../input");

fn distance(point1: (i32, i32), point2: (i32, i32)) -> i32 {
    (point1.0 - point2.0).abs() + (point1.1 - point2.1).abs()
}

fn parse_line(line: &str) -> (i32, i32) {
    let ints: Vec<i32> = line.split(", ").map(|s| s.parse().unwrap()).collect();

    (ints[0], ints[1])
}

fn main() {
    let coordinates: Vec<(i32, i32)> = INPUT.lines().map(|l| parse_line(l)).collect();

    let top_left = (
        coordinates.iter().map(|c| c.0).min().unwrap(),
        coordinates.iter().map(|c| c.1).min().unwrap(),
    );
    let bottom_right = (
        coordinates.iter().map(|c| c.0).max().unwrap(),
        coordinates.iter().map(|c| c.1).max().unwrap(),
    );

    let mut areas: HashMap<(i32, i32), i32> = HashMap::new();
    for x in (top_left.0 + 1)..(bottom_right.0 - 1) {
        for y in (top_left.1 + 1)..(bottom_right.1 - 1) {
            let mut distances: Vec<(i32, (i32, i32))> = coordinates
                .iter()
                .map(|c| (distance(*c, (x, y)), *c))
                .collect();

            distances.sort();
            if distances[0].0 != distances[1].0 {
                let closest = distances[0].1;
                *areas.entry(closest).or_default() += 1;
            }
        }
    }

    let largest_area = areas.values().max().unwrap();
    println!("{}", largest_area);
}
