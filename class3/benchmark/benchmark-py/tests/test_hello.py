from calculator import series
import pytest

def test_hello():
    assert "hello" == "hello"

def test_factorial():
    assert series.factorial(5) == 120

@pytest.mark.parametrize("n", [1,2,4,8,16,32])
def test_factorial_benchmark(benchmark, n):
    benchmark.pedantic(series.factorial, args=(n,), rounds=100, iterations=1000)
