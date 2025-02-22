use num_bigint::BigUint;
use num_traits::One;

pub fn factorial(n: u128) -> Result<u128, String> {
    if n == 0 {
        return Ok(1);
    }
    return Ok(n * factorial(n - 1).unwrap());
}

pub fn big_factorial(n: u32) -> BigUint {
    if n == 0 {
        return BigUint::one();
    }
    return n * big_factorial(n - 1);
}
