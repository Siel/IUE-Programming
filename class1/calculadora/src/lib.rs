pub fn suma(left: f64, right: f64) -> f64 {
    left + right
}

pub fn resta(left: f64, right: f64) -> f64 {
    left - right
}

pub fn multiplicacion(left: f64, right: f64) -> f64 {
    left * right
}

pub fn syntax() {
    let edad = 32;
    if edad >= 18 {
        println!("es mayor de edad")
    } else {
        println!("es menor de edad")
    }

    let frutas = vec!["mango", "banana", "manzana"];

    for fruta in frutas {
        println!("quiero una {}", fruta);
    }

    let mut count = 0;
    while count < 5 {
        println!("{}", count);
        count = count + 1;
    }
}
