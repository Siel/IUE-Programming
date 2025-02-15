# Class 1

## Introduction to the languages

**Python**: High-level, interpreted, dynamically typed, multi-paradigm, and garbage-collected programming language.  
**Rust**: Low-level, compiled, statically typed, multi-paradigm, and memory-safe programming language.

## Characteristics

### Python

**Pros:**

- Easy to learn, easy to read, and easy to write.
- Big community and extensive ecosystem.
- Strong support for scientific computing and machine learning (libraries like NumPy, Pandas, TensorFlow, Pytorch).

**Cons:**

- Slower performance due to being interpreted.
- Not suitable for direct hardware access (embedded systems, mobile apps).
- Less memory efficient for some applications.

### Rust

**Pros:**

- High performance due to compilation.
- Memory safety guarantees with its ownership system.
- Excellent support for concurrency and parallelism.
- Modern tooling with Cargo for dependency management.

**Cons:**

- Steeper learning curve due to strict compile-time checks and ownership model.
- Longer compilation times compared to interpreted languages.
- Smaller ecosystem compared to Python in certain domains.

## When to use

**Python:**

- **Best for:**  
  Rapid prototyping and scripting, data analysis, machine learning, and automation tasks.
- **Not ideal for:**  
  Performance-critical applications and low-level system programming.

**Rust:**

- **Best for:**  
  Systems programming, performance-critical applications, and projects requiring strong memory safety.
- **Not ideal for:**  
  Rapid prototyping or scripting tasks where quick iteration is a priority.

## How to install

### Python Installation:

1. **Download:**  
   Visit the [official Python website](https://www.python.org/) and download the installer for your OS.
2. **Install:**  
   Run the installer and follow the setup instructions. (On Windows, remember to check “Add Python to PATH”)
3. **Verify:**  
   Open a terminal/command prompt and run:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

### Managing Python Versions with pyenv

pyenv is a powerful tool that allows you to easily switch between multiple versions of Python. This is especially useful when different projects require different Python versions or when you need to test your code against various Python releases.

- **Installation:**

  **For macOS (using Homebrew):**

  ```bash
  brew update
  brew install pyenv
  ```

  **For Ubuntu:**

  ```bash
  curl https://pyenv.run | bash
  ```

  Alternatively, refer to the [pyenv GitHub repository](https://github.com/pyenv/pyenv) for installation instructions on other platforms.

- **Configuration:**

  Add the following lines to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):

  ```bash
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  ```

  Then, restart your shell or run `source ~/.bashrc` (or `source ~/.zshrc`).

- **Usage:**

  - **Install a Python version:**
    ```bash
    pyenv install 3.9.7
    ```
  - **Set a global Python version:**
    ```bash
    pyenv global 3.9.7
    ```
  - **Set a local Python version for a project:**
    In your project directory:
    ```bash
    pyenv local 3.9.7
    ```

- **Verifying the Python Version:**

  Check the active Python version with:

  ```bash
  python --version
  ```

### Rust Installation:

1. **Install Rustup:**  
   Open your terminal and run:
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
2. **Follow Prompts:**  
   Complete the installation as guided by the prompts.
3. **Verify:**  
   Run the following command to check:
   ```bash
   rustc --version
   ```

### Managing Rust Versions with rustup

rustup is the official toolchain installer and version manager for Rust, allowing you to easily install, update, and switch between multiple versions of the Rust compiler and its associated tools.

- **Installation:**

  For most platforms, install rustup using the following command:

  ```bash
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  ```

  Follow the on-screen instructions to complete the installation. This will install the latest stable version of Rust along with rustup.

- **Configuration:**

  After installation, ensure that the Rust binaries are added to your system's `PATH`. Typically, rustup automatically adds them, but if needed, add the following line to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):

  ```bash
  export PATH="$HOME/.cargo/bin:$PATH"
  ```

  Then reload your shell configuration:

  ```bash
  source ~/.bashrc   # or source ~/.zshrc
  ```

- **Usage:**

  - **Install a Specific Rust Version:**
    ```bash
    rustup toolchain install 1.84.0
    ```
  - **Set a Default (Global) Rust Version:**
    ```bash
    rustup default 1.84.0
    ```
  - **Set a Local Rust Version for a Project:**
    In your project directory, override the toolchain version with:
    ```bash
    rustup override set nightly
    ```
    This sets the Rust version for that specific directory without changing the global default.
  - **List Installed Rust Toolchains:**
    ```bash
    rustup toolchain list
    ```

- **Verifying the Rust Version:**

  Check the active Rust version with:

  ```bash
  rustc --version
  ```

## Package management

### Python Package Management with Poetry

Poetry is a modern dependency management and packaging tool for Python that automatically creates and manages a virtual environment for your project. It also allows you to specify the required Python version, helping to manage multiple Python versions across projects.

- **Installation of Poetry:**

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

  Alternatively, you can install it via pip:

  ```bash
  pip install poetry
  ```

- **Creating a New Project:**
  Poetry initializes a new project and sets up a virtual environment automatically:

  ```bash
  poetry new my_project
  cd my_project
  ```

- **Integration with Pyenv:**

  Poetry will use the active Python version from pyenv when creating a virtual environment. By specifying the Python version in your `pyproject.toml`, you ensure that the correct Python version is used. If the version specified is not installed, you can install it using pyenv before creating the project environment.

- **Managing the Virtual Environment:**
  Poetry automatically creates and uses a virtual environment for each project. You can check the environment details with:

  ```bash
  poetry env info
  ```

  To activate the virtual environment:

  ```bash
  poetry shell
  ```

  In your `pyproject.toml` file, you can specify the required Python version:

  ```toml
  [tool.poetry.dependencies]
  python = "^3.8"
  ```

- **Installing Dependencies:**
  To add a dependency, simply run:

  ```bash
  poetry add package_name
  ```

- **Running Commands in the Virtual Environment:**
  You can run commands within the environment without activating it manually:
  ```bash
  poetry run python your_script.py
  ```

### Rust Package Management with Cargo

Cargo is Rust’s built-in package manager and build system that simplifies managing your projects, dependencies, building, testing, and documentation.

#### Creating a New Project

- Create a new project with Cargo:
  ```bash
  cargo new my_project
  cd my_project
  ```
  This command generates a project directory with a default structure including a `Cargo.toml` file and a `src` folder containing `main.rs`.

#### Building and Running the Project

- **Build the project:**
  ```bash
  cargo build
  ```
- **Build for release (optimized build):**
  ```bash
  cargo build --release
  ```
- **Run the project:**
  ```bash
  cargo run
  ```

#### Adding Dependencies

- **Manually add dependencies:**  
  Edit the `Cargo.toml` file and add your desired crates under the `[dependencies]` section.
  ```toml
  [dependencies]
  serde = "1.0"
  ```
- **Using Cargo commands:**  
  If you have the `cargo-edit` extension installed, you can add dependencies from the command line:
  ```bash
  cargo add serde
  ```

#### Running Tests

- Execute all tests in your project:
  ```bash
  cargo test
  ```

#### Generating Documentation

- Generate and open documentation for your project:
  ```bash
  cargo doc --open
  ```

---

### How to Publish Your Package

Publishing your package allows you to share your work with the community. Below are instructions for publishing packages in both Rust and Python.

#### Publishing a Rust Package to crates.io

1. **Prepare Your Package**

   - Update `Cargo.toml` with complete metadata:
     ```toml
     [package]
     name = "my_package"
     version = "0.1.0"
     authors = ["Your Name <your.email@example.com>"]
     description = "A brief description of my package."
     repository = "https://github.com/yourusername/my_package"
     license = "MIT"
     ```
   - Test your package:
     ```bash
     cargo test
     cargo build --release
     ```

2. **Log In to crates.io**

   - Create an account on [crates.io](https://crates.io/).
   - Obtain your API token from your account and log in via Cargo:
     ```bash
     cargo login <your_api_token>
     ```
     Replace `<your_api_token>` with your actual token.

3. **Publish the Package**
   - Publish your package with:
     ```bash
     cargo publish
     ```
   - For subsequent updates, increment the version number in `Cargo.toml` before publishing.

#### Publishing a Python Package with Poetry

1. **Prepare Your Package**

   - Ensure your `pyproject.toml` contains all necessary metadata:
     ```toml
     [tool.poetry]
     name = "my_package"
     version = "0.1.0"
     description = "A brief description of my package."
     authors = ["Your Name <your.email@example.com>"]
     license = "MIT"
     homepage = "https://github.com/yourusername/my_package"
     repository = "https://github.com/yourusername/my_package"
     ```
   - Run tests and ensure your package works as expected.

2. **Build Your Package**

   - Build your package using Poetry:
     ```bash
     poetry build
     ```
   - This will create distribution files (e.g., `.tar.gz` and `.whl`) in the `dist/` directory.

3. **Publish to PyPI**
   - Ensure you have a PyPI account and obtain your API token from your account.
   - Configure Poetry to use your PyPI token:
     ```bash
     poetry config pypi-token.pypi <your_api_token>
     ```
     Replace `<your_api_token>` with your actual token.
   - Publish your package with:
     ```bash
     poetry publish --build
     ```
   - For testing, you can publish to TestPyPI:
     ```bash
     poetry publish --build -r testpypi
     ```

## Variables, Data Types, Operators, Expressions, Statements, and Control Structures

This section covers the fundamental building blocks of programming. We'll explore variables, data types, operators, expressions, statements, and control structures, with examples in both Python and Rust.

---

### Python

#### Variables & Type Flexibility

- **Definition:**  
  Variables in Python are dynamically typed, meaning their type is determined at runtime and can be changed.
- **Example:**

  ```python
  value = 42            # Initially an integer
  print(value)          # Output: 42

  value = "A string now"  # Reassigned to a string
  print(value)            # Output: A string now
  ```

#### Data Types and Collections

- **Primitive Data Types:**  
  `int`, `float`, `str`, `bool`
- **List (Ordered Collection):**
  ```python
  fruits = ["apple", "banana", "cherry"]
  print(fruits[1])  # Output: banana
  ```
- **Dictionary (Key-Value Store):**
  ```python
  person = {"name": "Alice", "age": 30}
  print(person["name"])  # Output: Alice
  ```

#### Operators & Expressions

- **Operators:**  
  Arithmetic (`+`, `-`, `*`, `/`, `%`), Comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`), Logical (`and`, `or`, `not`)
- **Example:**
  ```python
  a = 10
  b = 3
  sum_value = a + b         # Evaluates to 13
  is_equal = (a == b)       # Evaluates to False
  print(sum_value, is_equal)
  ```

#### Statements and Control Structures

- **Conditional Statements (if-elif-else):**
  ```python
  age = 20
  if age < 13:
      print("Child")
  elif age < 20:
      print("Teenager")
  else:
      print("Adult")
  ```
- **For Loop:**

  ```python
  # Iterating over a list
  for fruit in fruits:
      print(fruit)

  # Iterating using range
  for i in range(5):
      print(i)
  ```

- **While Loop:**
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```

---

### Rust

#### Variables, Explicit Type Annotations, and the `mut` Keyword

- **Definition:**  
  Variables in Rust are immutable by default. Use the `mut` keyword to allow mutation. Rust often requires explicit type annotations when the type cannot be inferred.
- **Example:**
  ```rust
  let x = 42;              // Immutable, type inferred as i32
  let mut y: i32 = 10;     // Mutable variable with explicit type annotation
  y = 20;
  println!("x: {}, y: {}", x, y);
  ```

#### Data Types and Collections

- **Primitive Data Types:**  
  `i32`, `f64`, `bool`, etc.
- **Vec (Dynamic Array):**
  ```rust
  let mut numbers: Vec<i32> = vec![1, 2, 3];
  numbers.push(4);
  println!("Numbers: {:?}", numbers);
  ```
- **HashMap (Key-Value Store):**

  ```rust
  use std::collections::HashMap;

  let mut person = HashMap::new();
  person.insert("name", "Alice");
  person.insert("age", 30);
  println!("Person: {:?}", person);
  ```

#### Operators & Expressions

- **Operators:**  
  Arithmetic (`+`, `-`, `*`, `/`, `%`), Comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`), Logical (`&&`, `||`, `!`)
- **Example:**
  ```rust
  let a = 10;
  let b = 3;
  let sum = a + b;           // 13
  let is_equal = a == b;       // false
  println!("Sum: {}, Equal: {}", sum, is_equal);
  ```

#### Statements and Control Structures

- **Conditional Statements (if):**
  ```rust
  let age = 20;
  if age < 13 {
      println!("Child");
  } else if age < 20 {
      println!("Teenager");
  } else {
      println!("Adult");
  }
  ```
- **Loop Constructs:**

  - **Infinite Loop with `loop`:**
    ```rust
    let mut count = 0;
    loop {
        if count >= 5 {
            break;
        }
        println!("Count: {}", count);
        count += 1;
    }
    ```
  - **While Loop:**
    ```rust
    let mut count = 0;
    while count < 5 {
        println!("Count: {}", count);
        count += 1;
    }
    ```
  - **For Loop with Iterators:**

    ```rust
    // Iterating over a range
    for i in 0..5 {
        println!("i: {}", i);
    }

    // Iterating over a vector using an iterator
    let fruits = vec!["apple", "banana", "cherry"];
    for fruit in fruits.iter() {
        println!("Fruit: {}", fruit);
    }

    // Iterating over a vector using enumerate
    for (index, fruit) in fruits.iter().enumerate() {
        println!("Index: {}, Fruit: {}", index, fruit);
    }
    ```

## Functions and Error Handling Basics

### Python

#### Defining Functions

Functions in Python are defined using the `def` keyword. Parameters can have default values to make them optional.

```python
def greet(name="Guest"):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Example usage:
print(greet("Alice"))  # Output: Hello, Alice!
print(greet())         # Output: Hello, Guest!
```

#### Lambda Functions

Lambda functions provide a concise way to write anonymous functions.

```python
# A lambda function to add two numbers
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
```

#### Basic Error Handling

Python uses try/except blocks to catch exceptions and handle errors gracefully.

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    return result

# Example usage:
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error message and None
```

---

### Rust

#### Defining Functions and Ownership Considerations

In Rust, functions require explicit type annotations. By default, function parameters are passed by value. Use references to borrow data and avoid transferring ownership.

```rust
// Function that borrows a string slice instead of taking ownership
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

fn main() {
    let name = String::from("Alice");
    // Passing a reference to the string to avoid moving ownership
    println!("{}", greet(&name));
}
```

#### Closures

Closures in Rust are similar to lambda functions in Python. They can capture variables from their environment.

```rust
fn main() {
    let x = 5;
    // Define a closure that adds its parameter to x
    let add_to_x = |num: i32| x + num;
    println!("Result: {}", add_to_x(10));  // Output: 15
}
```

#### Basic Error Handling with `Result`

Rust uses the `Result` type for error handling instead of exceptions. Functions that might fail return a `Result`, which must be handled by the caller.

```rust
// Function that performs division and returns a Result
fn divide(a: i32, b: i32) -> Result<i32, &'static str> {
    if b == 0 {
        Err("Error: Division by zero")
    } else {
        Ok(a / b)
    }
}

fn main() {
    // Handling the result using pattern matching
    match divide(10, 2) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => println!("{}", e),
    }

    // Using the ? operator in a function that returns a Result
    fn try_divide(a: i32, b: i32) -> Result<i32, &'static str> {
        let result = divide(a, b)?;
        Ok(result)
    }

    println!("Try Divide: {:?}", try_divide(10, 0));  // Output: Error message
}
```
