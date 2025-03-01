mod shapes;

use shapes::{Color, Rectangle, Shape, Triangle};

fn main() {
    let triangle = Triangle::new(3.0, 4.0);
    let rectangle = Rectangle::new(3.0, 4.0);
    // triangle.report();
    // rectangle.report();

    triangle.color();

    report_shape(triangle);

    report_shape(rectangle);
}

fn report_shape(shape: impl Shape + Color) {
    shape.report();

    println!(
        "My area is {} and my color is {}",
        shape.area(),
        shape.color()
    );
}
