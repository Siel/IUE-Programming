pub trait Shape {
    fn area(&self) -> f64;
    fn report(&self);
}

pub trait Color {
    fn color(&self) -> &'static str {
        "red"
    }
}

impl Color for Triangle {}

impl Color for Rectangle {
    fn color(&self) -> &'static str {
        "blue"
    }
}

pub struct Triangle {
    base: f64,
    height: f64,
}

pub struct Rectangle {
    width: f64,
    height: f64,
}

impl Triangle {
    pub fn new(base: f64, height: f64) -> Triangle {
        Triangle { base, height }
    }
    pub fn color(&self) -> &'static str {
        "red"
    }
}

impl Rectangle {
    pub fn new(width: f64, height: f64) -> Rectangle {
        Rectangle { width, height }
    }
}

impl Shape for Triangle {
    fn area(&self) -> f64 {
        0.5 * self.base * self.height
    }

    fn report(&self) {
        println!(
            "I am a triangle with base {} and height {}",
            self.base, self.height
        );
    }
}

impl Shape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn report(&self) {
        println!(
            "I am a rectangle with width {} and height {}",
            self.width, self.height
        );
    }
}
