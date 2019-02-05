const INPUT: &str = include_str!("../input");

fn reacts(c1: char, c2: char) -> bool {
    return (c1 != c2) && (c1.to_uppercase().to_string() == c2.to_uppercase().to_string());
}

fn main() {
    let polymer = INPUT.trim();

    let mut stack = Vec::new();
    for c in polymer.chars() {
        if stack.is_empty() {
            stack.push(c);
            continue;
        }

        if reacts(c, stack[stack.len() - 1]) {
            stack.pop();
        } else {
            stack.push(c);
        }
    }

    println!("{}", stack.len());
}
