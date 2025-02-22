fn main() {
    let result = calculator::factorial(8);
    match result {
        Ok(val) => println!("{}", val),
        Err(err) => println!("{}", err),
    };
    // let result = calculator::factorial(-1).unwrap();
    // println!("{}", result);
}
