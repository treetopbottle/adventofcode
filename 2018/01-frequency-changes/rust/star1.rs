fn main() {
    let input = include_str!("../input");

    let mut sum = 0;
    for line in input.lines() {
        sum += line.parse::<i32>().unwrap();
    }

    println!("{}", sum);
}
