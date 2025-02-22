use calculator::big_factorial;

use num_bigint::BigUint;
use std::time::Instant;

fn main() {
    let numbers = vec![500, 600, 700, 800];
    let mut results = vec![BigUint::ZERO, BigUint::ZERO, BigUint::ZERO, BigUint::ZERO];
    let start = Instant::now();

    results.iter_mut().enumerate().for_each(|(i, r)| {
        *r = big_factorial(numbers[i]);
    });

    for (i, result) in results.iter().enumerate() {
        println!("El factorial de {} es {}", numbers[i], result)
    }

    println!("Calculated all factorials in {:?}", start.elapsed());
}
