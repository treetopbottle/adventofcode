use std::cmp::min;
use std::cmp::max;

const INPUT: &str = include_str!("../input");

fn distance(point1: (i32, i32), point2: (i32, i32)) -> i32 {
    return (point1.0 - point2.0).abs() + (point1.1 - point2.1).abs()
}

fn main() {
    let mut top_left = (i32::max_value(), i32::max_value());
    let mut bottom_right = (i32::min_value(), i32::min_value());
    let mut coordinates: Vec<(i32, i32)> = Vec::new();
    for line in INPUT.lines() {
        let ints: Vec<i32> = line.split(", ")
            .map(|s| s.parse()
            .unwrap())
            .collect();

        top_left = (
            min(top_left.0, ints[0]),
            min(top_left.1, ints[1])
        );
        bottom_right = (
            max(bottom_right.0, ints[0]),
            max(bottom_right.1, ints[1])
        );
        coordinates.push((ints[0], ints[1]));
    }

    const MAX_DISTANCE: i32 = 10000;
    let mut region_size = 0;
    for x in (top_left.0)..(bottom_right.0) {
        for y in (top_left.1)..(bottom_right.1) {
            let mut total_distance = 0;
            for coordinate in coordinates.as_slice() {
                total_distance += distance(*coordinate, (x, y));
            }
            if total_distance < MAX_DISTANCE {
                region_size += 1;
            }
        }
    }

    println!("{}", region_size);
}
