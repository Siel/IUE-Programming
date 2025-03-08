///! # Math Utils
///!
///! `math_utils` contiene funciones matemáticas útiles.

/// #Calcula el factorial de un número.
///
/// ## argumentos:
/// * `n` - El número del cual se quiere calcular el factorial.
///
/// ## retorna:
/// El factorial de `n`.
///
/// ## Ejemplos:
///
///
/// ```
/// use doctest_rs::math_utils::factorial;
/// assert_eq!(factorial(0), 1);
/// assert_eq!(factorial(1), 1);
/// assert_eq!(factorial(2), 2);
/// assert_eq!(factorial(3), 6);
/// assert_eq!(factorial(4), 24);
/// assert_eq!(factorial(5), 120);
/// ```
pub fn factorial(n: u64) -> u64 {
    match n {
        0 | 1 => 1,
        _ => n * factorial(n - 1),
    }
}
