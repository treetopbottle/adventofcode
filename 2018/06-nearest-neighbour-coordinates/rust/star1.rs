use std::cmp::min;
use std::cmp::max;
use std::collections::HashMap;

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

    let mut largest_area = i32::min_value();
    let mut areas: HashMap<(i32, i32), i32> = HashMap::new();
    for x in (top_left.0 + 1)..(bottom_right.0 - 1) {
        for y in (top_left.1 + 1)..(bottom_right.1 - 1) {
            let mut min_distance = i32::max_value();
            let mut closests: Vec<(i32, i32)> = Vec::new();
            for coordinate in coordinates.as_slice() {
                if distance(*coordinate, (x, y)) < min_distance {
                    min_distance = distance(*coordinate, (x, y));
                    closests = Vec::new();
                    closests.push(*coordinate);
                } else if distance(*coordinate, (x, y)) == min_distance {
                    min_distance = distance(*coordinate, (x, y));
                    closests.push(*coordinate);
                }
            }
            if closests.len() == 1 {
                let closest = closests[0];
                *areas.entry(closest).or_default() += 1;
                largest_area = max(largest_area, areas[&closest]);
            }
        }
    }

    println!("{}", largest_area);
}
