# Pynary

## Installation

Currently, installation is not perfect, but will be better once this library is available for installation via pip.

1. Install Rust (and cargo)
2. Install maturin
3. Clone this repo
4. Create a virtual environment (MUST BE NAMED "env") in the directory of the repo
5. Activate your virtual environment
6. Run "maturin develop"
7. pynary will be installed in your venv

## Usage

- Unit tests can be run using pytest in the root of the directory
- Rudimentary (extremely so) benchmarks can be completed using the benchmark.py file.
- There is one class associated with this library, which is BinaryArray. This class accepts an array of either boolean or integer values (0 or 1).
