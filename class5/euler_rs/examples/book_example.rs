use ode_solver::euler::solve_system;

pub mod ode_solver;

fn book_example(t: f64, x: &Vec<f64>) -> Vec<f64> {
    let dx_dt = (1.0 - 2.0 * t) * x[0];
    vec![dx_dt]
}

fn main() {
    let y0 = vec![1.0];
    let ti = 0.0;
    let tf = 0.9;
    let h = 0.3;

    let (t_values, y_values) = solve_system(book_example, y0, ti, tf, h);

    for i in 0..t_values.len() {
        println!("t: {}, x: {}", t_values[i], y_values[i][0]);
    }
}
