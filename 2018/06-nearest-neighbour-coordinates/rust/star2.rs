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

    const MAX_DISTANCE: i32 = 10000;
    let mut region_size = 0;
    for x in (top_left.0)..(bottom_right.0) {
        for y in (top_left.1)..(bottom_right.1) {
            let total_distance: i32 = coordinates.iter().map(|c| distance(*c, (x, y))).sum();

            if total_distance < MAX_DISTANCE {
                region_size += 1;
            }
        }
    }

    println!("{}", region_size);
}
