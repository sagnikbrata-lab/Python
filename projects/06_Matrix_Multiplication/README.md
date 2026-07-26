# Matrix Multiplication

A Python implementation of general matrix multiplication for matrices of arbitrary dimensions.

## Description

This program multiplies two matrices of dimensions **n × m** and **m × p** using the standard three-loop algorithm taught in introductory linear algebra.

The program:
- Verifies whether multiplication is possible.
- Computes the product for matrices of compatible dimensions.
- Displays the resulting matrix.
- Reports when multiplication is not defined.

## Concepts Practised

- Functions
- Nested loops
- Two-dimensional lists
- Matrix indexing
- Dimension validation
- Basic algorithm implementation

## Mathematical Background

For matrices

- A of size n × m
- B of size m × p

their product C = AB is an n × p matrix where

C[i][j] = Σ A[i][k] × B[k][j]

for k = 0 to m − 1.

## Example

```
A × B

[94, 100]
[229, 244]
[364, 388]
[499, 532]
```

## Future Improvements

- Accept matrix input from the user.
- Validate empty or irregular matrices.
- Improve output formatting.
- Add NumPy implementation for comparison.
- Measure execution time for large matrices.

---

Created as part of my Python learning journey during my B.Sc. Physics. I have just learnt the algo for matrix multiplication in class and wanted to write code for the same.