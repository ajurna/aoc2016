use std::fmt::format;
use md5::{compute, Digest};

const PUZZLE: &str = "ffykfhsq";
fn main() {
    let mut i = -1;
    let mut password1 = Vec::new();
    let mut password2: [String; 8] = [String::new(), String::new(), String::new(), String::new(), String::new(), String::new(), String::new(), String::new()];

    let mut next: String;
    let mut sum: Digest;
    let mut formatted: String;
    let mut j = 0;
    loop {
        i += 1;
        next = PUZZLE.to_owned() + &*i.to_string();
        if i %1000000 ==0 {
            println!("{i}")
        }
        sum = compute(next);
        formatted = format!("{:x}", sum);
        if formatted.starts_with("00000") {
            let p1 = formatted.get(5..6).unwrap().to_owned();
            let p2 = formatted.get(6..7).unwrap().to_owned();
            if p1.parse::<u8>().is_ok() {
                let idx = p1.parse::<u8>().unwrap() as usize;
                if idx < password2.len() {
                    if password2[idx] == "" {
                        password2[idx] = p2;
                        j += 1;
                        if j == 8 {
                            break;
                        }
                    }
                }
            }
            if password1.len() < 8 {
                password1.push(p1)
            }
        }
    }
    let result = password1.join("");
    println!("Part 1: {result:?}");
    let result = password2.join("");
    println!("Part 2: {result:?}");

}
